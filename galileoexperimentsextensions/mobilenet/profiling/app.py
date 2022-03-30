import base64
from typing import Dict

import redis
import requests
from galileo.shell.shell import Galileo, ClientGroup
from galileoexperiments.api.model import ProfilingWorkloadConfiguration
from galileoexperiments.api.profiling import ProfilingApplication
from kubernetes import client
from kubernetes.client import V1ResourceRequirements, V1EnvVar, V1EnvVarSource, V1ObjectFieldSelector


def _prepare_image(url: str):
    r = requests.get(url)
    r.raise_for_status()
    return base64.b64encode(r.content).decode('utf-8')


def _get_image(url: str) -> str:
    data = _prepare_image(url)
    return '{"picture": "%s"}' % data


def _spawn_zone_group(zone: str, clients: int, g: Galileo, image_url: str, fn_name: str) -> ClientGroup:
    return _spawn_group(g, clients, fn_name, f'{fn_name}-{zone}', image_url=image_url, labels={'galileo_zone': zone})


def _spawn_group(g: Galileo, clients: int, fn_name: str, service_name: str, image_url: str, labels: dict = None):
    path = f'/function/{fn_name}'
    return g.spawn(service_name, clients,
                   parameters={'method': 'post', 'path': path, 'kwargs': {'data': _get_image(image_url)}},
                   worker_labels=labels)


class MobilenetProfilingApplication(ProfilingApplication):

    def spawn_group(self, rds: redis.Redis, galileo: Galileo, config: ProfilingWorkloadConfiguration) -> ClientGroup:
        clients = config.params['exp']['requests']['n_clients']
        zone = config.zone
        image_url = config.params['service']['image_url']
        fn_name = config.params['service']['name']
        return _spawn_group(galileo, clients, fn_name, f'{fn_name}-{zone}', image_url=image_url,
                            labels={'galileo_zone': zone})

    def pod_factory(self, pod_name: str, image: str, resource_requests: Dict) -> client.V1Container:
        return client.V1Container(
            image=image,
            name=pod_name,
            ports=[
                client.V1ContainerPort(
                    name="function-port", container_port=8080
                )
            ],
            resources=V1ResourceRequirements(
                requests=resource_requests
            ),
            env=[
                V1EnvVar('NODE_NAME', value_from=V1EnvVarSource(
                    field_ref=(V1ObjectFieldSelector(field_path='spec.nodeName')))),
                V1EnvVar('MODEL_STORAGE', 'local'),
                V1EnvVar('MODEL_FILE', '/home/app/function/data/mobilenet.tflite'),
                V1EnvVar('LABELS_FILE', '/home/app/function/data/labels.txt'),
                V1EnvVar('IMAGE_STORAGE', 'request')
            ]
        )
