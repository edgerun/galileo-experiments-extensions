import logging

from galileo.shell.shell import init
from galileo.worker.context import Context
from galileoexperiments.api.model import ScenarioWorkloadConfiguration
from galileoexperiments.experiment.scenario.run import run_scenario_workload

from galileoexperimentsextensions.humandetection.app import HumanDetectionProfilingApplication

logger = logging.getLogger(__name__)


def main():
    logging.basicConfig(level=logging._nameToLevel['INFO'])
    creator = 'test'
    humandetection_image = 'edgerun/humandetection:1.0.0'
    app_names = {
        humandetection_image: 'humandetection'
    }

    master_node = 'master-node'

    # node to service mapping including the number of service instances
    services = {
        'test-node': {
            humandetection_image: 1
        }
    }

    # maps nodes that should host applications to zones
    zone_mapping = {
        'test-node': 'test-zone'
    }

    params = {}

    # parameters for each image (used to initialize the clients)
    app_params = {
        humandetection_image: {
            'service': {
                'name': 'humandetection',
                # Human in picture
                'location': 'https://i.imgur.com/PJuAkgB.jpg',
                # No human in picture
                # 'location': 'https://i.imgur.com/Jr8O96d.jpg',
                'remote': True
            }
        }
    }

    profiling_apps = {
        humandetection_image: HumanDetectionProfilingApplication()
    }

    # Instantiate galileo context that includes all dependencies needed to execute an experiment
    ctx = Context()
    rds = ctx.create_redis()
    g = init(rds)

    # contains 4 requests
    test_profile = 'data/profiles/test.pkl'

    # client profiles, each starts one client that sends to the zone's load balancer
    profiles = {
        'test-zone': {
            humandetection_image: [test_profile, test_profile]
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

        profiles=profiles
    )

    run_scenario_workload(config)


if __name__ == '__main__':
    main()
