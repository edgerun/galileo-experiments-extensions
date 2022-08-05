import logging

from galileo.shell.shell import init
from galileo.worker.context import Context
from galileoexperiments.api.model import ScenarioWorkloadConfiguration
from galileoexperiments.experiment.scenario.run import run_scenario_workload

from galileoexperimentsextensions.gundetection.app import GunDetectionProfilingApplication
from galileoexperimentsextensions.humandetection.app import HumanDetectionProfilingApplication
from galileoexperimentsextensions.maskdetection.app import MaskDetectionProfilingApplication
from galileoexperimentsextensions.taxidriversafetyapp.app import TaxiDriverSafetyAppProfilingApplication

logger = logging.getLogger(__name__)


def main():
    logging.basicConfig(level=logging._nameToLevel['INFO'])
    creator = 'test'
    taxidriversafetyapp_image = 'edgerun/taxidriversafetyapp:1.0.0'
    humandetection_image = 'edgerun/humandetection:1.0.0'
    gundetection_image = 'edgerun/gundetection:1.0.0'
    maskdetection_image = 'edgerun/maskdetection:1.0.0'
    app_names = {
        taxidriversafetyapp_image: 'taxidriversafetyapp'
    }

    master_node = 'master-node'

    # node to service mapping including the number of service instances
    services = {
        'test-node': {
            humandetection_image: 1,
            gundetection_image: 1,
            maskdetection_image: 1,
            taxidriversafetyapp_image: 1
        }
    }

    # maps nodes that should host applications to zones
    zone_mapping = {
        'test-node': 'test-zone'
    }

    params = {}

    # parameters for each image (used to initialize the clients)
    app_params = {
        taxidriversafetyapp_image: {
            'service': {
                'name': 'taxidriversafetyapp',
                'location': 'https://i.imgur.com/bqnrbv6.jpg',
                # 'location': 'https://i.imgur.com/XWPElmP.jpg',
                'remote': True
            }
        },
        humandetection_image: {
            'service': {
                'name': 'humandetection'
            }
        },
        maskdetection_image: {
            'service': {
                'name': 'maskdetection'
            }
        },
        gundetection_image: {
            'service': {
                'name': 'gundetection'
            }
        }
    }

    profiling_apps = {
        taxidriversafetyapp_image: TaxiDriverSafetyAppProfilingApplication(),
        humandetection_image: HumanDetectionProfilingApplication(),
        maskdetection_image: MaskDetectionProfilingApplication(),
        gundetection_image: GunDetectionProfilingApplication()
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
            taxidriversafetyapp_image: [test_profile, test_profile]
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
