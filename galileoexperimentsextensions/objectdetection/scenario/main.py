import logging

from galileo.shell.shell import init
from galileo.worker.context import Context
from galileoexperiments.api.model import ScenarioWorkloadConfiguration
from galileoexperiments.experiment.scenario.run import run_scenario_workload

from galileoexperimentsextensions.objectdetection.app import ObjectDetectionProfilingApplication

logger = logging.getLogger(__name__)


def main():
    logging.basicConfig(level=logging._nameToLevel['INFO'])
    creator = 'test'
    objectdetection_image = 'edgerun/objectdetection:1.0.0'
    app_names = {
        objectdetection_image: 'objectdetection'
    }

    master_node = 'master-node'

    # node to service mapping including the number of service instances
    services = {
        'test-node': {
            objectdetection_image: 1
        }
    }

    # maps nodes that should host applications to zones
    zone_mapping = {
        'test-node': 'test-zone'
    }

    params = {}

    # parameters for each image (used to initialize the clients)
    app_params = {
        objectdetection_image: {
            'service': {
                'name': 'objectdetection',
                # Objects in picture
                'location': 'https://i.imgur.com/pLIicD8.jpg',
                'remote': True
            }
        }
    }

    profiling_apps = {
        objectdetection_image: ObjectDetectionProfilingApplication()
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
            objectdetection_image: [test_profile, test_profile]
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
