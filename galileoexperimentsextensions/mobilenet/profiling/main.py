import logging
import sys

from galileo.shell.shell import init
from galileo.worker.context import Context
from galileoexperiments.api.model import ProfilingWorkloadConfiguration
from galileoexperiments.experiment.profiling.run import run_profiling_workload

from galileoexperimentsextensions.mobilenet.app import MobilenetProfilingApplication

logger = logging.getLogger(__name__)


def main():
    logging.basicConfig(level=logging._nameToLevel['INFO'])

    if len(sys.argv) != 6:
        raise ValueError(
            'Program takes exactly six arguments: <creator> <host> <container-image> <zone> <master-node>')

    creator = sys.argv[1]
    host = sys.argv[2]
    image = sys.argv[3]
    zone = sys.argv[4]
    master_node = sys.argv[5]

    # Instantiate galileo context that includes all dependencies needed to execute an experiment
    ctx = Context()
    rds = ctx.create_redis()
    g = init(rds)

    # Configure mobilenet specific parameters (i.e., image_url) and define the function name
    params = {
        'service': {
            'name': 'mobilenet',
            'location': 'https://i.imgur.com/0jx0gP8.png',
            'remote': True,
        }
    }

    # Instantiate the Profiling Application that contains methods that spawn a container and return a ClientGroup
    mobilenet_profiling_app = MobilenetProfilingApplication()

    workload_config = ProfilingWorkloadConfiguration(
        creator=creator,
        app_name='mobilenet',
        host=host,
        image=image,
        master_node=master_node,
        zone=zone,
        context=g,
        params=params,
        profiling_app=mobilenet_profiling_app,
        no_pods=1,
        n=10,
        ia=0.5,
        n_clients=1,
    )
    run_profiling_workload(workload_config)


if __name__ == '__main__':
    main()
