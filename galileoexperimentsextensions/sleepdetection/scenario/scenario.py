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
    # container image
    image = sys.argv[2]
    zones = sys.argv[3]
    master_node = sys.argv[4]
    # function name
    name = sys.argv[5]
    profiles = sys.argv[6]
    picture = sys.argv[7]

    # each zone gets unique function to avoid that load balancer sends randomly requests across cluster
    fn_a = f'{name}-zone-a'
    fn_b = f'{name}-zone-b'
    fn_c = f'{name}-zone-c'

    app_names = {
        fn_a: image
    }

    zone_mapping = {
        "eb-a-controller": 'zone-a'
    }

    services = {
        "eb-a-controller": {
            fn_a: 1
        }
    }

    app_params = {
        fn_a: {
            'service': {
                'name': fn_a,
                'location': picture,
                'remote': True,
            }
        }
    }

    profiles_0 = profiles + '/0_pickups.pkl'
    profiles_1 = profiles + '/1_pickups.pkl'
    profiles_2 = profiles + '/3_pickups.pkl'

    # client profiles, each starts one client that sends to the zone's load balancer
    profiles_all = {
        'zone-a': {
            fn_a: [profiles_0]
        },
    }

    if zones == "2":
        app_params = {
            fn_a: {
                'service': {
                    'name': fn_a,
                    'location': picture,
                    'remote': True,
                }
            },
            fn_b: {
                'service': {
                    'name': fn_b,
                    'location': picture,
                    'remote': True,
                }
            }
        }
        app_names = {
            fn_a: image,
            fn_b: image
        }

        zone_mapping = {
            "eb-a-controller": 'zone-a',
            "eb-b-controller": 'zone-b'
        }
        services = {
            "eb-a-controller": {
                fn_a: 1
            },
            "eb-b-controller": {
                fn_b: 1
            }
        }

        profiles_all = {
            'zone-a': {
                fn_a: [profiles_0]
            },
            'zone-b': {
                fn_b: [profiles_1]
            },
        }

    if zones == "3":
        app_params = {
            fn_a: {
                'service': {
                    'name': fn_a,
                    'location': picture,
                    'remote': True,
                }
            },
            fn_b: {
                'service': {
                    'name': fn_b,
                    'location': picture,
                    'remote': True,
                }
            },
            fn_c: {
                'service': {
                    'name': fn_c,
                    'location': picture,
                    'remote': True,
                }
            }
        }
        app_names = {
            fn_a: image,
            fn_b: image,
            fn_c: image
        }

        zone_mapping = {
            "eb-a-controller": 'zone-a',
            "eb-b-controller": 'zone-b',
            "eb-c-vm-0": 'zone-c'
        }
        services = {
            "eb-a-controller": {
                fn_a: 1
            },
            "eb-b-controller": {
                fn_b: 1
            },
            "eb-c-vm-0": {
                fn_c: 1
            }
        }
        profiles_all = {
            'zone-a': {
                fn_a: [profiles_0],
                fn_c: [profiles_2]
            },
            'zone-b': {
                fn_b: [profiles_1]
            }
        }

    params = {
        'name': name + "_" + profiles.rsplit('/', 1)[-1]
    }

    profiling_apps = {
        fn_a: SleepDetectionProfilingApplication(),
        fn_b: SleepDetectionProfilingApplication(),
        fn_c: SleepDetectionProfilingApplication()
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
