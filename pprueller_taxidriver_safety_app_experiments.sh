# taxidriversafetyapp new_york_1x1_1x1
python -m galileoexperimentsextensions.taxidriversafetyapp.scenario.scenario pruellerpaul 1 eb-k3s-master taxidriversafetyapp-1-zone-min data/profiles/new_york_1x1_1x1_min https://i.imgur.com/CubSR2U.jpg
sleep 60
python -m galileoexperimentsextensions.taxidriversafetyapp.scenario.scenario pruellerpaul 1 eb-k3s-master taxidriversafetyapp-1-zone-avg data/profiles/new_york_1x1_1x1_avg https://i.imgur.com/CubSR2U.jpg
sleep 60
python -m galileoexperimentsextensions.taxidriversafetyapp.scenario.scenario pruellerpaul 1 eb-k3s-master taxidriversafetyapp-1-zone-max data/profiles/new_york_1x1_1x1_max https://i.imgur.com/CubSR2U.jpg
sleep 60

# taxidriversafetyapp new_york_2x2_2x1
python -m galileoexperimentsextensions.taxidriversafetyapp.scenario.scenario pruellerpaul 2 eb-k3s-master taxidriversafetyapp-1-zone-min data/profiles/new_york_1x1_1x1_min https://i.imgur.com/CubSR2U.jpg
sleep 60
python -m galileoexperimentsextensions.taxidriversafetyapp.scenario.scenario pruellerpaul 2 eb-k3s-master taxidriversafetyapp-1-zone-avg data/profiles/new_york_1x1_1x1_avg https://i.imgur.com/CubSR2U.jpg
sleep 60
python -m galileoexperimentsextensions.taxidriversafetyapp.scenario.scenario pruellerpaul 2 eb-k3s-master taxidriversafetyapp-1-zone-max data/profiles/new_york_1x1_1x1_max https://i.imgur.com/CubSR2U.jpg
sleep 60