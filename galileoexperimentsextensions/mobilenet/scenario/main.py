import logging
import sys

from galileo.shell.shell import init
from galileo.worker.context import Context
from galileoexperiments.api.model import ScenarioWorkloadConfiguration
from galileoexperiments.experiment.scenario.run import run_scenario_workload

from galileoexperimentsextensions.mobilenet.app import MobilenetProfilingApplication

logger = logging.getLogger(__name__)


def main():
    logging.basicConfig(level=logging._nameToLevel['INFO'])
    creator = 'test'
    mobilenet_image = 'edgerun/mobilenet-inference:1.1'
    app_names = {
        mobilenet_image: 'mobilenet'
    }

    master_node = 'eb-k3s-master'

    services = {
        'eb-b-xeon-0': {
            mobilenet_image: 2
        },
        'eb-a-controller': {
            mobilenet_image: 1
        }
    }

    zone_a = 'zone-a'
    zone_b = 'zone-b'
    zone_mapping = {
        'eb-b-xeon-0': zone_b,
        'eb-a-controller': zone_a
    }

    params = {}

    app_params = {
        mobilenet_image: {
            'service': {
                'name': 'mobilenet',
                'image_url': 'https://i.imgur.com/0jx0gP8.png'
            }
        }
    }

    profiling_apps = {
        mobilenet_image: MobilenetProfilingApplication()
    }

    # Instantiate galileo context that includes all dependencies needed to execute an experiment
    ctx = Context()
    rds = ctx.create_redis()
    g = init(rds)

    lb_ips = {
        zone_a: '192.168.1.2',
        zone_b: '192.168.0.101'
    }

    test_profile = 'data/profiles/test.pkl'
    profiles = {
        zone_a: {
            mobilenet_image: [test_profile, test_profile],
        },
        zone_b: {
            mobilenet_image: [test_profile]
        }
    }

    config = ScenarioWorkloadConfiguration(
        creator=creator,
        app_names=app_names,
        master_node=master_node,
        services=services,
        zone_mapping=zone_mapping,
        params=params,
        app_params=app_params,
        profiling_apps=profiling_apps,
        context=g,

        lb_ips=lb_ips,
        profiles=profiles
    )

    run_scenario_workload(config)

if __name__ == '__main__':
    main()
