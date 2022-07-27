import logging
import sys

from galileo.shell.shell import init
from galileo.worker.context import Context
from galileoexperiments.api.model import ProfilingWorkloadConfiguration
from galileoexperiments.experiment.profiling.run import run_profiling_workload

from galileoexperimentsextensions.gundetection.app import GunDetectionProfilingApplication

logger = logging.getLogger(__name__)


def main():
    logging.basicConfig(level=logging._nameToLevel['INFO'])

    if len(sys.argv) != 6:
        raise ValueError(
            'Program takes exactly five arguments: <creator> <host> <container-image> <zone> <master-node>')

    creator = sys.argv[1]
    host = sys.argv[2]
    image = sys.argv[3]
    zone = sys.argv[4]
    master_node = sys.argv[5]

    # Instantiate galileo context that includes all dependencies needed to execute an experiment
    ctx = Context()
    rds = ctx.create_redis()
    g = init(rds)

    # Configure Gundetection specific parameters (i.e., image_url) and define the function name
    params = {
        'service': {
            'name': 'gundetection',
            # Gun in picture
            'location': 'https://i.imgur.com/OacG55z.jpg',
            # No Gun in picture
            # 'location': 'https://i.imgur.com/bqnrbv6.jpg',
            'remote': True,
        }
    }

    # Instantiate the Profiling Application that contains methods that spawn a container and return a ClientGroup
    gundetection_profiling_app = GunDetectionProfilingApplication()

    workload_config = ProfilingWorkloadConfiguration(
        creator=creator,
        app_name='gundetection',
        host=host,
        image=image,
        master_node=master_node,
        zone=zone,
        context=g,
        params=params,
        profiling_app=gundetection_profiling_app,
        no_pods=1,
        n=10,
        ia=0.5,
        n_clients=1
    )
    run_profiling_workload(workload_config)


if __name__ == '__main__':
    main()
