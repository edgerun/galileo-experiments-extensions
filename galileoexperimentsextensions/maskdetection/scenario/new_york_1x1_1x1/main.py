import logging

from galileo.shell.shell import init
from galileo.worker.context import Context
from galileoexperiments.api.model import ScenarioWorkloadConfiguration
from galileoexperiments.experiment.scenario.run import run_scenario_workload

from galileoexperimentsextensions.maskdetection.app import MaskDetectionProfilingApplication

logger = logging.getLogger(__name__)


def main():
    logging.basicConfig(level=logging._nameToLevel['INFO'])
    creator = 'pruellerpaul'
    maskdetection_image = 'edgerun/maskdetection:1.1.0'
    app_names = {
        maskdetection_image: 'maskdetection'
    }

    master_node = 'eb-k3s-master'

    # node to service mapping including the number of service instances
    services = {
        'eb-a-controller': {
            maskdetection_image: 1
        }
    }

    # maps nodes that should host applications to zones
    zone_mapping = {
        'eb-a-controller': 'zone-a'
    }

    params = {}

    # parameters for each image (used to initialize the clients)
    app_params = {
        maskdetection_image: {
            'service': {
                'name': 'maskdetection',
                # Mask in picture
                'location': 'https://i.imgur.com/al98FL9.jpg',
                # No mask in picture
                # 'location': 'https://i.imgur.com/bqnrbv6.jpg',
                'remote': True,
            }
        }
    }

    profiling_apps = {
        maskdetection_image: MaskDetectionProfilingApplication()
    }

    # Instantiate galileo context that includes all dependencies needed to execute an experiment
    ctx = Context()
    rds = ctx.create_redis()
    g = init(rds)

    basePath = "/your/base/path/"
    # contains requests for first cloudlet
    new_york_1x1_1x1_profile_min = basePath + 'data/profiles/new_york_1x1_1x1_min/0_pickups.pkl'
    new_york_1x1_1x1_profile_avg = basePath + 'data/profiles/new_york_1x1_1x1_avg/0_pickups.pkl'
    new_york_1x1_1x1_profile_max = basePath + 'data/profiles/new_york_1x1_1x1_max/0_pickups.pkl'

    # client profiles, each starts one client that sends to the zone's load balancer
    profiles_min = {
        'zone-a': {
            maskdetection_image: [new_york_1x1_1x1_profile_min]
        }
    }
    profiles_avg = {
        'zone-a': {
            maskdetection_image: [new_york_1x1_1x1_profile_avg]
        }
    }
    profiles_max = {
        'zone-a': {
            maskdetection_image: [new_york_1x1_1x1_profile_max]
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
        profiles=profiles_min,
        context=g
    )

    # run min request scenario
    run_scenario_workload(config)

    # run avg request scenario
    # config.profiles = profiles_avg
    # run_scenario_workload(config)

    # run max request scenario
    # config.profiles = profiles_max
    # run_scenario_workload(config)


if __name__ == '__main__':
    main()
