import logging
import sys

from galileo.shell.shell import init
from galileo.worker.context import Context
from galileoexperiments.api.model import ScenarioWorkloadConfiguration
from galileoexperiments.experiment.scenario.run import run_scenario_workload

from galileoexperimentsextensions.taxidriversafetyapp.app import TaxiDriverSafetyAppProfilingApplication
from galileoexperimentsextensions.humandetection.app import HumanDetectionProfilingApplication
from galileoexperimentsextensions.maskdetection.app import MaskDetectionProfilingApplication
from galileoexperimentsextensions.gundetection.app import GunDetectionProfilingApplication

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

    # each zone gets unique function to avoid that load balancer sends randomly requests across cluster
    fn_a_taxidriversafetyapp = f'{name}-zone-a'
    fn_b_taxidriversafetyapp = f'{name}-zone-b'
    fn_c_taxidriversafetyapp = f'{name}-zone-c'
    fn_a_humandetection = 'humandetection-zone-a'
    fn_b_humandetection = 'humandetection-zone-b'
    fn_c_humandetection = 'humandetection-zone-c'
    fn_a_gundetection = 'gundetection-zone-a'
    fn_b_gundetection = 'gundetection-zone-b'
    fn_c_gundetection = 'gundetection-zone-c'
    fn_a_maskdetection = 'maskdetection-zone-a'
    fn_b_maskdetection = 'maskdetection-zone-b'
    fn_c_maskdetection = 'maskdetection-zone-c'

    taxidriversafetyapp_image = 'edgerun/taxidriversafetyapp:1.1.0'
    humandetection_image = 'edgerun/humandetection:1.1.0'
    gundetection_image = 'edgerun/gundetection:1.1.0'
    maskdetection_image = 'edgerun/maskdetection:1.1.0'

    app_names = {
        fn_a_humandetection: humandetection_image,
        fn_a_gundetection: gundetection_image,
        fn_a_maskdetection: maskdetection_image,
        fn_a_taxidriversafetyapp: taxidriversafetyapp_image,
    }

    app_params = {
        fn_a_taxidriversafetyapp: {
            'service': {
                'name': fn_a_taxidriversafetyapp,
                'location': picture,
                'remote': True,
            }
        }
    }

    zone_mapping = {
        "eb-a-controller": 'zone-a'
    }

    services = {
        "eb-a-controller": {
            fn_a_taxidriversafetyapp: 1,
            fn_a_humandetection: 1,
            fn_a_gundetection: 1,
            fn_a_maskdetection: 1,
        },
    }

    profiles_0 = profiles + '/test.pkl'
    profiles_1 = profiles + '/test.pkl'
    profiles_2 = profiles + '/test.pkl'

    # client profiles, each starts one client that sends to the zone's load balancer
    profiles_all = {
        'zone-a': {
            fn_a_taxidriversafetyapp: [profiles_0]
        },
    }

    if zones == "2":
        app_names = {
            fn_a_humandetection: humandetection_image,
            fn_a_gundetection: gundetection_image,
            fn_a_maskdetection: maskdetection_image,
            fn_a_taxidriversafetyapp: taxidriversafetyapp_image,
            fn_b_humandetection: humandetection_image,
            fn_b_gundetection: gundetection_image,
            fn_b_maskdetection: maskdetection_image,
            fn_b_taxidriversafetyapp: taxidriversafetyapp_image,
        }

        app_params = {
            fn_a_taxidriversafetyapp: {
                'service': {
                    'name': fn_a_taxidriversafetyapp,
                    'location': picture,
                    'remote': True,
                }
            },
            fn_b_taxidriversafetyapp: {
                'service': {
                    'name': fn_b_taxidriversafetyapp,
                    'location': picture,
                    'remote': True,
                }
            }
        }

        zone_mapping = {
            "eb-a-controller": 'zone-a',
            "eb-b-controller": 'zone-b'
        }
        services = {
            "eb-a-controller": {
                fn_a_taxidriversafetyapp: 1,
                fn_a_humandetection: 1,
                fn_a_gundetection: 1,
                fn_a_maskdetection: 1,
            },
            "eb-b-controller": {
                fn_b_taxidriversafetyapp: 1,
                fn_b_humandetection: 1,
                fn_b_gundetection: 1,
                fn_b_maskdetection: 1,
            },
        }

        profiles_all = {
            'zone-a': {
                fn_a_taxidriversafetyapp: [profiles_0]
            },
            'zone-b': {
                fn_a_taxidriversafetyapp: [profiles_1]
            },
        }
    if zones == "3":
        app_names = {
            fn_a_humandetection: humandetection_image,
            fn_a_gundetection: gundetection_image,
            fn_a_maskdetection: maskdetection_image,
            fn_a_taxidriversafetyapp: taxidriversafetyapp_image,
            fn_b_humandetection: humandetection_image,
            fn_b_gundetection: gundetection_image,
            fn_b_maskdetection: maskdetection_image,
            fn_b_taxidriversafetyapp: taxidriversafetyapp_image,
            fn_c_humandetection: humandetection_image,
            fn_c_gundetection: gundetection_image,
            fn_c_maskdetection: maskdetection_image,
            fn_c_taxidriversafetyapp: taxidriversafetyapp_image,
        }

        app_params = {
            fn_a_taxidriversafetyapp: {
                'service': {
                    'name': fn_a_taxidriversafetyapp,
                    'location': picture,
                    'remote': True,
                }
            },
            fn_b_taxidriversafetyapp: {
                'service': {
                    'name': fn_b_taxidriversafetyapp,
                    'location': picture,
                    'remote': True,
                }
            },
            fn_c_taxidriversafetyapp: {
                'service': {
                    'name': fn_c_taxidriversafetyapp,
                    'location': picture,
                    'remote': True,
                }
            }
        }

        zone_mapping = {
            "eb-a-controller": 'zone-a',
            "eb-b-controller": 'zone-b',
            "eb-c-vm-0": 'zone-c'
        }

        services = {
            "eb-a-controller": {
                fn_a_taxidriversafetyapp: 1,
                fn_a_humandetection: 1,
                fn_a_gundetection: 1,
                fn_a_maskdetection: 1,
            },
            "eb-b-controller": {
                fn_b_taxidriversafetyapp: 1,
                fn_b_humandetection: 1,
                fn_b_gundetection: 1,
                fn_b_maskdetection: 1,
            },
            "eb-c-vm-0": {
                fn_c_taxidriversafetyapp: 1,
                fn_c_humandetection: 1,
                fn_c_gundetection: 1,
                fn_c_maskdetection: 1,
            }
        }

        profiles_all = {
            'zone-a': {
                fn_a_taxidriversafetyapp: [profiles_0],
                fn_c_taxidriversafetyapp: [profiles_2]
            },
            'zone-b': {
                fn_b_taxidriversafetyapp: [profiles_1]
            }
        }


    params = {
        'name': name + "_" + profiles.rsplit('/', 1)[-1]
    }

    profiling_apps = {
        fn_a_taxidriversafetyapp: TaxiDriverSafetyAppProfilingApplication(),
        fn_a_humandetection: HumanDetectionProfilingApplication(),
        fn_a_gundetection: GunDetectionProfilingApplication(),
        fn_a_maskdetection: MaskDetectionProfilingApplication(),
        fn_b_taxidriversafetyapp: TaxiDriverSafetyAppProfilingApplication(),
        fn_b_humandetection: HumanDetectionProfilingApplication(),
        fn_b_gundetection: GunDetectionProfilingApplication(),
        fn_b_maskdetection: MaskDetectionProfilingApplication(),
        fn_c_taxidriversafetyapp: TaxiDriverSafetyAppProfilingApplication(),
        fn_c_humandetection: HumanDetectionProfilingApplication(),
        fn_c_gundetection: GunDetectionProfilingApplication(),
        fn_c_maskdetection: MaskDetectionProfilingApplication(),
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
