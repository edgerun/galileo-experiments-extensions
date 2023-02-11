# humandetection new_york_1x1_1x1
python -m galileoexperimentsextensions.humandetection.scenario.scenario pruellerpaul edgerun/humandetection:1.1.0 1 eb-k3s-master humandetection-1-zone-1x1-min data/profiles/new_york_1x1_1x1_min https://i.imgur.com/ztir9ww.jpg
sleep 60
python -m galileoexperimentsextensions.humandetection.scenario.scenario pruellerpaul edgerun/humandetection:1.1.0 1 eb-k3s-master humandetection-1-zone-1x1-avg data/profiles/new_york_1x1_1x1_avg https://i.imgur.com/ztir9ww.jpg
sleep 60
python -m galileoexperimentsextensions.humandetection.scenario.scenario pruellerpaul edgerun/humandetection:1.1.0 1 eb-k3s-master humandetection-1-zone-1x1-max data/profiles/new_york_1x1_1x1_max https://i.imgur.com/ztir9ww.jpg
sleep 60

# humandetection new_york_1x1_05x05
python -m galileoexperimentsextensions.humandetection.scenario.scenario pruellerpaul edgerun/humandetection:1.1.0 3 eb-k3s-master humandetection-3-zones-1x1-min data/profiles/new_york_1x1_05x05_min https://i.imgur.com/ztir9ww.jpg
sleep 60
python -m galileoexperimentsextensions.humandetection.scenario.scenario pruellerpaul edgerun/humandetection:1.1.0 3 eb-k3s-master humandetection-3-zones-1x1-avg data/profiles/new_york_1x1_05x05_avg https://i.imgur.com/ztir9ww.jpg
sleep 60
python -m galileoexperimentsextensions.humandetection.scenario.scenario pruellerpaul edgerun/humandetection:1.1.0 3 eb-k3s-master humandetection-3-zones-1x1-max data/profiles/new_york_1x1_05x05_max https://i.imgur.com/ztir9ww.jpg
sleep 60

# gundetection new_york_1x1_1x1
python -m galileoexperimentsextensions.gundetection.scenario.scenario pruellerpaul edgerun/gundetection:1.1.0 1 eb-k3s-master gundetection-1-zone-1x1-min data/profiles/new_york_1x1_1x1_min https://i.imgur.com/ztir9ww.jpg
sleep 60
python -m galileoexperimentsextensions.gundetection.scenario.scenario pruellerpaul edgerun/gundetection:1.1.0 1 eb-k3s-master gundetection-1-zone-1x1-avg data/profiles/new_york_1x1_1x1_avg https://i.imgur.com/ztir9ww.jpg
sleep 60
python -m galileoexperimentsextensions.gundetection.scenario.scenario pruellerpaul edgerun/gundetection:1.1.0 1 eb-k3s-master gundetection-1-zone-1x1-max data/profiles/new_york_1x1_1x1_max https://i.imgur.com/ztir9ww.jpg
sleep 60

# gundetection new_york_1x1_05x05
python -m galileoexperimentsextensions.gundetection.scenario.scenario pruellerpaul edgerun/gundetection:1.1.0 3 eb-k3s-master gundetection-3-zones-1x1-min data/profiles/new_york_1x1_05x05_min https://i.imgur.com/ztir9ww.jpg
sleep 60
python -m galileoexperimentsextensions.gundetection.scenario.scenario pruellerpaul edgerun/gundetection:1.1.0 3 eb-k3s-master gundetection-3-zones-1x1-avg data/profiles/new_york_1x1_05x05_avg https://i.imgur.com/ztir9ww.jpg
sleep 60
python -m galileoexperimentsextensions.gundetection.scenario.scenario pruellerpaul edgerun/gundetection:1.1.0 3 eb-k3s-master gundetection-3-zones-1x1-max data/profiles/new_york_1x1_05x05_max https://i.imgur.com/ztir9ww.jpg
sleep 60

# mask detection new_york_2x2_1x1
python -m galileoexperimentsextensions.maskdetection.scenario.scenario pruellerpaul edgerun/maskdetection:1.1.0 3 eb-k3s-master maskdetection-3-zones-2x2-min data/profiles/new_york_2x2_1x1_min https://i.imgur.com/LpfkZ4D.jpg
sleep 60
python -m galileoexperimentsextensions.maskdetection.scenario.scenario pruellerpaul edgerun/maskdetection:1.1.0 3 eb-k3s-master maskdetection-3-zones-2x2-avg data/profiles/new_york_2x2_1x1_avg https://i.imgur.com/LpfkZ4D.
sleep 60
python -m galileoexperimentsextensions.maskdetection.scenario.scenario pruellerpaul edgerun/maskdetection:1.1.0 3 eb-k3s-master maskdetection-3-zones-2x2-max data/profiles/new_york_2x2_1x1_max https://i.imgur.com/LpfkZ4D.jpg
sleep 60

# mask detection new_york_2x2_2x1
python -m galileoexperimentsextensions.maskdetection.scenario.scenario pruellerpaul edgerun/maskdetection:1.1.0 2 eb-k3s-master maskdetection-2-zones-2x2-min data/profiles/new_york_2x2_2x1_min https://i.imgur.com/LpfkZ4D.jpg
sleep 60
python -m galileoexperimentsextensions.maskdetection.scenario.scenario pruellerpaul edgerun/maskdetection:1.1.0 2 eb-k3s-master maskdetection-2-zones-2x2-avg data/profiles/new_york_2x2_2x1_avg https://i.imgur.com/LpfkZ4D.jpg
sleep 60
python -m galileoexperimentsextensions.maskdetection.scenario.scenario pruellerpaul edgerun/maskdetection:1.1.0 2 eb-k3s-master maskdetection-2-zones-2x2-max data/profiles/new_york_2x2_2x1_max https://i.imgur.com/LpfkZ4D.jpg
sleep 60

# pose estimation new_york_2x2_1x1
python -m galileoexperimentsextensions.poseestimation.scenario.scenario pruellerpaul edgerun/poseestimation:1.1.0 3 eb-k3s-master poseestimation-3-zones-2x2-min data/profiles/new_york_2x2_1x1_min https://i.imgur.com/ztir9ww.jpg
sleep 60
python -m galileoexperimentsextensions.poseestimation.scenario.scenario pruellerpaul edgerun/poseestimation:1.1.0 3 eb-k3s-master poseestimation-3-zones-2x2-avg data/profiles/new_york_2x2_1x1_avg https://i.imgur.com/ztir9ww.jpg
sleep 60
python -m galileoexperimentsextensions.poseestimation.scenario.scenario pruellerpaul edgerun/poseestimation:1.1.0 3 eb-k3s-master poseestimation-3-zones-2x2-max data/profiles/new_york_2x2_1x1_max https://i.imgur.com/ztir9ww.jpg
sleep 60

# pose estimation new_york_2x2_2x1
python -m galileoexperimentsextensions.poseestimation.scenario.scenario pruellerpaul edgerun/poseestimation:1.1.0 2 eb-k3s-master poseestimation-2-zones-2x2-min data/profiles/new_york_2x2_2x1_min https://i.imgur.com/ztir9ww.jpg
sleep 60
python -m galileoexperimentsextensions.poseestimation.scenario.scenario pruellerpaul edgerun/poseestimation:1.1.0 2 eb-k3s-master poseestimation-2-zones-2x2-avg data/profiles/new_york_2x2_2x1_avg https://i.imgur.com/ztir9ww.jpg
sleep 60
python -m galileoexperimentsextensions.poseestimation.scenario.scenario pruellerpaul edgerun/poseestimation:1.1.0 2 eb-k3s-master poseestimation-2-zones-2x2-max data/profiles/new_york_2x2_2x1_max https://i.imgur.com/ztir9ww.jpg
sleep 60

# sleepdetection new_york_2x2_1x1
python -m galileoexperimentsextensions.sleepdetection.scenario.scenario pruellerpaul edgerun/sleepdetection:1.1.0 3 eb-k3s-master sleepdetection-3-zones-2x2-min data/profiles/new_york_2x2_1x1_min https://i.imgur.com/ztir9ww.jpg
sleep 60
python -m galileoexperimentsextensions.sleepdetection.scenario.scenario pruellerpaul edgerun/sleepdetection:1.1.0 3 eb-k3s-master sleepdetection-3-zones-2x2-avg data/profiles/new_york_2x2_1x1_avg https://i.imgur.com/ztir9ww.jpg
sleep 60
python -m galileoexperimentsextensions.sleepdetection.scenario.scenario pruellerpaul edgerun/sleepdetection:1.1.0 3 eb-k3s-master sleepdetection-3-zones-2x2-max data/profiles/new_york_2x2_1x1_max https://i.imgur.com/ztir9ww.jpg
sleep 60

# sleepdetection new_york_2x2_2x1
python -m galileoexperimentsextensions.sleepdetection.scenario.scenario pruellerpaul edgerun/sleepdetection:1.1.0 2 eb-k3s-master sleepdetection-2-zones-2x2-min data/profiles/new_york_2x2_2x1_min https://i.imgur.com/ztir9ww.jpg
sleep 60
python -m galileoexperimentsextensions.sleepdetection.scenario.scenario pruellerpaul edgerun/sleepdetection:1.1.0 2 eb-k3s-master sleepdetection-2-zones-2x2-avg data/profiles/new_york_2x2_2x1_avg https://i.imgur.com/ztir9ww.jpg
sleep 60
python -m galileoexperimentsextensions.sleepdetection.scenario.scenario pruellerpaul edgerun/sleepdetection:1.1.0 2 eb-k3s-master sleepdetection-2-zones-2x2-max data/profiles/new_york_2x2_2x1_max https://i.imgur.com/ztir9ww.jpg
sleep 60

# object detection new_york_1x1_1x1
python -m galileoexperimentsextensions.objectdetection.scenario.scenario pruellerpaul edgerun/objectdetection:1.1.0 3 eb-k3s-master objectdetection-3-zones-1x1-min data/profiles/new_york_1x1_1x1_min https://i.imgur.com/LpfkZ4D.jpg
sleep 60
python -m galileoexperimentsextensions.objectdetection.scenario.scenario pruellerpaul edgerun/objectdetection:1.1.0 3 eb-k3s-master objectdetection-3-zones-1x1-avg data/profiles/new_york_1x1_1x1_avg https://i.imgur.com/LpfkZ4D.
sleep 60
python -m galileoexperimentsextensions.objectdetection.scenario.scenario pruellerpaul edgerun/objectdetection:1.1.0 3 eb-k3s-master objectdetection-3-zones-1x1-max data/profiles/new_york_1x1_1x1_max https://i.imgur.com/LpfkZ4D.jpg
sleep 60

# object detection new_york_1x1_05x05
python -m galileoexperimentsextensions.objectdetection.scenario.scenario pruellerpaul edgerun/objectdetection:1.1.0 3 eb-k3s-master objectdetection-3-zones-1x1-min data/profiles/new_york_1x1_05x05_min https://i.imgur.com/ztir9ww.jpg
sleep 60
python -m galileoexperimentsextensions.objectdetection.scenario.scenario pruellerpaul edgerun/objectdetection:1.1.0 3 eb-k3s-master objectdetection-3-zones-1x1-avg data/profiles/new_york_1x1_05x05_avg https://i.imgur.com/ztir9ww.jpg
sleep 60
python -m galileoexperimentsextensions.objectdetection.scenario.scenario pruellerpaul edgerun/objectdetection:1.1.0 3 eb-k3s-master objectdetection-3-zones-1x1-max data/profiles/new_york_1x1_05x05_max https://i.imgur.com/ztir9ww.jpg
sleep 60