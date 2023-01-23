import logging
import sys

from galileo.shell.shell import init
from galileo.worker.context import Context
from galileoexperiments.api.model import ScenarioWorkloadConfiguration
from galileoexperiments.experiment.scenario.run import run_scenario_workload

from galileoexperimentsextensions.taxidriversafetyapp.app import TaxiDriverSafetyAppProfilingApplication

logger = logging.getLogger(__name__)


def main():
    logging.basicConfig(level=logging._nameToLevel['INFO'])
    if len(sys.argv) != 7:
        raise ValueError(
            'Program takes exactly 7 arguments: <creator> <zones> <master-node> <name> <profiles> <picture>')

    creator = sys.argv[1]
    zones = sys.argv[2]
    master_node = sys.argv[3]
    name = sys.argv[4]
    profiles = sys.argv[5]
    picture = sys.argv[6]


    taxidriversafetyapp_image = 'edgerun/taxidriversafetyapp:1.1.0'
    humandetection_image = 'edgerun/humandetection:1.1.0'
    gundetection_image = 'edgerun/gundetection:1.1.0'
    maskdetection_image = 'edgerun/maskdetection:1.1.0'

    app_names = {
        taxidriversafetyapp_image: "taxidriversafetyapp",
        humandetection_image: "humandetection",
        gundetection_image: "gundetection",
        maskdetection_image: "maskdetection",
    }

    zone_mapping = {
        "eb-a-controller": 'zone-a'
    }
    services = {
        "eb-a-controller": {
            taxidriversafetyapp_image: 1,
            humandetection_image: 1,
            gundetection_image: 1,
            maskdetection_image: 1,
        }
    }

    profiles_0 = profiles + '/0_pickups.pkl'
    profiles_1 = profiles + '/1_pickups.pkl'
    profiles_2 = profiles + '/2_pickups.pkl'

    # client profiles, each starts one client that sends to the zone's load balancer
    profiles_all = {
        'zone-a': {
            taxidriversafetyapp_image: [profiles_0]
        },
    }

    if zones == "2":
        zone_mapping = {
            "eb-a-controller": 'zone-a',
            "eb-b-controller": 'zone-b'
        }
        services = {
            "eb-a-controller": {
                taxidriversafetyapp_image: 1,
                humandetection_image: 1,
                gundetection_image: 1,
                maskdetection_image: 1,
            },
            "eb-b-controller": {
                taxidriversafetyapp_image: 1,
                humandetection_image: 1,
                gundetection_image: 1,
                maskdetection_image: 1,
            }
        }

        profiles_all = {
            'zone-a': {
                taxidriversafetyapp_image: [profiles_0]
            },
            'zone-b': {
                taxidriversafetyapp_image: [profiles_1]
            },
        }
    if zones == "3":
        zone_mapping = {
            "eb-a-controller": 'zone-a',
            "eb-b-controller": 'zone-b',
            "eb-c-vm-0": 'zone-c'
        }
        services = {
            "eb-a-controller": {

                taxidriversafetyapp_image: 1,
                humandetection_image: 1,
                gundetection_image: 1,
                maskdetection_image: 1,
            },
            "eb-b-controller": {

                taxidriversafetyapp_image: 1,
                humandetection_image: 1,
                gundetection_image: 1,
                maskdetection_image: 1,
            },
            "eb-c-vm-0": {

                taxidriversafetyapp_image: 1,
                humandetection_image: 1,
                gundetection_image: 1,
                maskdetection_image: 1,
            }
        }
        profiles_all = {
            'zone-a': {
                taxidriversafetyapp_image: [profiles_0]
            },
            'zone-b': {
                taxidriversafetyapp_image: [profiles_1]
            },
            'zone-c': {
                taxidriversafetyapp_image: [profiles_2]
            },
        }


    params = {
        'name': name
    }

    app_params = {
        taxidriversafetyapp_image: {
            'service': {
                'name': name,
                'location': picture,
                'remote': True,
            }
        }
    }

    profiling_apps = {
        taxidriversafetyapp_image: TaxiDriverSafetyAppProfilingApplication()
    }

    # Instantiate galileo context that includes all dependencies needed to execute an experiment
    ctx = Context()
    rds = ctx.create_redis()
    g = init(rds)

    config = ScenarioWorkloadConfiguration(
        creator=creator,
        app_names=app_names,
        master_node=master_node,
        services=services,
        zone_mapping=zone_mapping,
        params=params,
        app_params=app_params,
        profiling_apps=profiling_apps,
        profiles=profiles_all,
        context=g
    )

    run_scenario_workload(config)

if __name__ == '__main__':
    main()
