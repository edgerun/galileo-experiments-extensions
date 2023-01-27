import json

import pandas
from galileojp.k3s import K3SGateway
import warnings
from influxdb_client.client.warnings import MissingPivotFunction

warnings.simplefilter("ignore", MissingPivotFunction)

class EdgebenchGateway(K3SGateway):
    pass

def getTraces(exp_id):
    print(exp_id)
    gw = EdgebenchGateway.from_env()
    traces = gw.traces(exp_id)
    traces.to_csv(exp_id + "_traces.csv")
    return traces


def getTelem(exp_id):
    print(exp_id)
    gw = EdgebenchGateway.from_env()
    telemetry = gw.telemetry(exp_id)
    telemetry.to_csv(exp_id + "_telem.csv")
    return telemetry

def main():
    # maskdetection 2x2 2x1 min: 202301271722-ad26
    # maskdetection 2x2 2x1 avg: 202301271733-d9a2
    # maskdetection 2x2 2x1 max: 202301271745-8fb6
    # humandetection 1x1 1x1 min: 202301271758-38b8
    # humandetection 1x1 1x1 avg: 202301271810-714d
    # humandetection 1x1 1x1 max: 202301271822-e2d4
    # pose estimation 2x2 2x1 min:202301271856-3ab3
    # pose estimation 2x2 2x1 avg:
    # pose estimation 2x2 2x1 max:
    exp_ids = ['202301271722-ad26', '202301271733-d9a2', '202301271745-8fb6',
               '202301271758-38b8', '202301271810-714d', '202301271822-e2d4',
               '202301271856-3ab3']
    for exp_id in exp_ids:
        try:
            traces = pandas.read_csv(exp_id + "_traces.csv")
        except:
            traces = getTraces(exp_id)
        try:
            telemetry = pandas.read_csv(exp_id + "_telem.csv")
        except:
            telemetry = getTelem(exp_id)

if __name__ == '__main__':
    main()