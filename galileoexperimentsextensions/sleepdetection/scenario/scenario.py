import logging
import sys

from galileo.shell.shell import init
from galileo.worker.context import Context
from galileoexperiments.api.model import ScenarioWorkloadConfiguration
from galileoexperiments.experiment.scenario.run import run_scenario_workload

from galileoexperimentsextensions.sleepdetection.app import SleepDetectionProfilingApplication

logger = logging.getLogger(__name__)


def main():
    logging.basicConfig(level=logging._nameToLevel['INFO'])
    if len(sys.argv) != 8:
        raise ValueError(
            'Program takes exactly 7 arguments: <creator> <container-image> <zones> <master-node> <name> <profiles> <picture>')

    creator = sys.argv[1]
    image = sys.argv[2]
    zones = sys.argv[3]
    master_node = sys.argv[4]
    name = sys.argv[5]
    profiles = sys.argv[6]
    picture = sys.argv[7]

    app_names = {
        image: name
    }

    zone_mapping = {
        "eb-a-controller": 'zone-a'
    }
    services = {
        "eb-a-controller": {
            image: 1
        }
    }

    profiles_0 = profiles + '/0_pickups.pkl'
    profiles_1 = profiles + '/1_pickups.pkl'
    profiles_2 = profiles + '/2_pickups.pkl'

    # client profiles, each starts one client that sends to the zone's load balancer
    profiles_all = {
        'zone-a': {
            image: [profiles_0]
        },
    }

    if zones == "2":
        zone_mapping = {
            "eb-a-controller": 'zone-a',
            "eb-b-controller": 'zone-b'
        }
        services = {
            "eb-a-controller": {
                image: 1
            },
            "eb-b-controller": {
                image: 1
            }
        }

        profiles_all = {
            'zone-a': {
                image: [profiles_0]
            },
            'zone-b': {
                image: [profiles_1]
            },
        }
    if zones == "3":
        zone_mapping = {
            "eb-a-controller": 'zone-a',
            "eb-b-controller": 'zone-b',
            "eb-c-vm-0": 'zone-a'
        }
        services = {
            "eb-a-controller": {
                image: 1
            },
            "eb-b-controller": {
                image: 1
            },
            "eb-c-vm-0": {
                image: 1
            }
        }
        profiles_all = {
            'zone-a': {
                image: [profiles_0]
            },
            'zone-b': {
                image: [profiles_1]
            },
            'zone-c': {
                image: [profiles_2]
            },
        }


    params = {
        'name': name
    }

    app_params = {
        image: {
            'service': {
                'name': name,
                'location': picture,
                'remote': True,
            }
        }
    }

    profiling_apps = {
        image: SleepDetectionProfilingApplication()
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
