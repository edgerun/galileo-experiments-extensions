import logging

from galileo.shell.shell import init
from galileo.worker.context import Context
from galileoexperiments.api.model import ScenarioWorkloadConfiguration
from galileoexperiments.experiment.scenario.run import run_scenario_workload

from galileoexperimentsextensions.sleepdetection.app import SleepDetectionProfilingApplication

logger = logging.getLogger(__name__)


def main():
    logging.basicConfig(level=logging._nameToLevel['INFO'])
    creator = 'test'
    sleepdetection_image = 'edgerun/sleepdetection:1.0.0'
    app_names = {
        sleepdetection_image: 'sleepdetection'
    }

    master_node = 'master-node'

    # node to service mapping including the number of service instances
    services = {
        'test-node': {
            sleepdetection_image: 1
        }
    }

    # maps nodes that should host applications to zones
    zone_mapping = {
        'test-node': 'test-zone'
    }

    params = {}

    # parameters for each image (used to initialize the clients)
    app_params = {
        sleepdetection_image: {
            'service': {
                'name': 'sleepdetection',
                # Sleeping person in picture
                'location': 'https://i.imgur.com/bqnrbv6.jpg',
                # No sleeping person in picture
                # 'location': 'https://i.imgur.com/XWPElmP.jpg',
                'remote': True
            }
        }
    }

    profiling_apps = {
        sleepdetection_image: SleepDetectionProfilingApplication()
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
            sleepdetection_image: [test_profile, test_profile]
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
