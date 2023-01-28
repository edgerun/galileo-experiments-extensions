# mask detection new_york_2x2_2x1 (DONE)
# python -m galileoexperimentsextensions.maskdetection.scenario.scenario pruellerpaul edgerun/maskdetection:1.1.0 2 eb-k3s-master maskdetection-2-zones-min data/profiles/new_york_2x2_2x1_min https://i.imgur.com/LpfkZ4D.jpg
# python -m galileoexperimentsextensions.maskdetection.scenario.scenario pruellerpaul edgerun/maskdetection:1.1.0 2 eb-k3s-master maskdetection-2-zones-avg data/profiles/new_york_2x2_2x1_avg https://i.imgur.com/LpfkZ4D.jpg
# python -m galileoexperimentsextensions.maskdetection.scenario.scenario pruellerpaul edgerun/maskdetection:1.1.0 2 eb-k3s-master maskdetection-2-zones-max data/profiles/new_york_2x2_2x1_max https://i.imgur.com/LpfkZ4D.jpg

# humandetection new_york_1x1_1x1
python -m galileoexperimentsextensions.humandetection.scenario.scenario pruellerpaul edgerun/humandetection:1.1.0 1 eb-k3s-master humandetection-1-zone-min data/profiles/new_york_1x1_1x1_min https://i.imgur.com/ztir9ww.jpg
sleep 10
python -m galileoexperimentsextensions.humandetection.scenario.scenario pruellerpaul edgerun/humandetection:1.1.0 1 eb-k3s-master humandetection-1-zone-avg data/profiles/new_york_1x1_1x1_avg https://i.imgur.com/ztir9ww.jpg
sleep 10
python -m galileoexperimentsextensions.humandetection.scenario.scenario pruellerpaul edgerun/humandetection:1.1.0 1 eb-k3s-master humandetection-1-zone-max data/profiles/new_york_1x1_1x1_max https://i.imgur.com/ztir9ww.jpg
sleep 10

# mask detection new_york_2x2_1x1 (don't work yet with zone-c mapping)
# python -m galileoexperimentsextensions.maskdetection.scenario.scenario pruellerpaul edgerun/maskdetection:1.1.0 3 eb-k3s-master maskdetection-3-zones-min data/profiles/new_york_2x2_1x1_min https://i.imgur.com/LpfkZ4D.jpg
# python -m galileoexperimentsextensions.maskdetection.scenario.scenario pruellerpaul edgerun/maskdetection:1.1.0 3 eb-k3s-master maskdetection-3-zones-avg data/profiles/new_york_2x2_1x1_avg https://i.imgur.com/LpfkZ4D.jpg
# python -m galileoexperimentsextensions.maskdetection.scenario.scenario pruellerpaul edgerun/maskdetection:1.1.0 3 eb-k3s-master maskdetection-3-zones-max data/profiles/new_york_2x2_1x1_max https://i.imgur.com/LpfkZ4D.jpg

# humandetection new_york_1x1_05x05 (don't work yet with zone-c mapping)
# python -m galileoexperimentsextensions.humandetection.scenario.scenario pruellerpaul edgerun/humandetection:1.1.0 3 eb-k3s-master humandetection-3-zones-min data/profiles/new_york_1x1_05x05_min https://i.imgur.com/ztir9ww.jpg
# python -m galileoexperimentsextensions.humandetection.scenario.scenario pruellerpaul edgerun/humandetection:1.1.0 3 eb-k3s-master humandetection-3-zones-avg data/profiles/new_york_1x1_05x05_avg https://i.imgur.com/ztir9ww.jpg
# python -m galileoexperimentsextensions.humandetection.scenario.scenario pruellerpaul edgerun/humandetection:1.1.0 3 eb-k3s-master humandetection-3-zones-max data/profiles/new_york_1x1_05x05_max https://i.imgur.com/ztir9ww.jpg

# pose estimation new_york_2x2_2x1
python -m galileoexperimentsextensions.poseestimation.scenario.scenario pruellerpaul edgerun/poseestimation:1.1.0 2 eb-k3s-master poseestimation-2-zones-min data/profiles/new_york_2x2_2x1_min https://i.imgur.com/ztir9ww.jpg
sleep 10
python -m galileoexperimentsextensions.poseestimation.scenario.scenario pruellerpaul edgerun/poseestimation:1.1.0 2 eb-k3s-master poseestimation-2-zones-avg data/profiles/new_york_2x2_2x1_avg https://i.imgur.com/ztir9ww.jpg
sleep 10
python -m galileoexperimentsextensions.poseestimation.scenario.scenario pruellerpaul edgerun/poseestimation:1.1.0 2 eb-k3s-master poseestimation-2-zones-max data/profiles/new_york_2x2_2x1_max https://i.imgur.com/ztir9ww.jpg
