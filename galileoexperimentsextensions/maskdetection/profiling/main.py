import logging
import sys

from galileo.shell.shell import init
from galileo.worker.context import Context
from galileoexperiments.api.model import ProfilingWorkloadConfiguration
from galileoexperiments.experiment.profiling.run import run_profiling_workload

from galileoexperimentsextensions.maskdetection.app import MaskDetectionProfilingApplication

logger = logging.getLogger(__name__)


def main():
    logging.basicConfig(level=logging._nameToLevel['INFO'])

    if len(sys.argv) != 6:
        raise ValueError(
            'Program takes exactly five arguments: <creator> <host> <container-image> <zone> <master-node> <picture>')

    creator = sys.argv[1]
    host = sys.argv[2]
    image = sys.argv[3]
    zone = sys.argv[4]
    master_node = sys.argv[5]
    picture = sys.argv[6]

    # Instantiate galileo context that includes all dependencies needed to execute an experiment
    ctx = Context()
    rds = ctx.create_redis()
    g = init(rds)

    # Configure maskdetection specific parameters (i.e., image_url) and define the function name
    params = {
        'service': {
            'name': f'{host}-maskdetection',
            'location': picture,
            'remote': True,
        }
    }

    # Instantiate the Profiling Application that contains methods that spawn a container and return a ClientGroup
    maskdetection_profiling_app = MaskDetectionProfilingApplication()

    workload_config = ProfilingWorkloadConfiguration(
        creator=creator,
        app_name='maskdetection',
        host=host,
        image=image,
        master_node=master_node,
        zone=zone,
        context=g,
        params=params,
        profiling_app=maskdetection_profiling_app,
        no_pods=1,
        n=100,
        ia=2,
        n_clients=1
    )
    run_profiling_workload(workload_config)


if __name__ == '__main__':
    main()
