python -m galileoexperimentsextensions.maskdetection.profiling.main pruellerpaul eb-a-controller edgerun/maskdetection:1.1.0 zone-a eb-k3s-master https://i.imgur.com/LpfkZ4D.jpg
sleep 10
python -m galileoexperimentsextensions.maskdetection.profiling.main pruellerpaul eb-b-controller edgerun/maskdetection:1.1.0 zone-b eb-k3s-master https://i.imgur.com/LpfkZ4D.jpg
sleep 10
python -m galileoexperimentsextensions.maskdetection.profiling.main pruellerpaul eb-c-vm-0 edgerun/maskdetection:1.1.0 zone-a eb-k3s-master https://i.imgur.com/LpfkZ4D.jpg
sleep 10

python -m galileoexperimentsextensions.humandetection.profiling.main pruellerpaul eb-a-controller edgerun/humandetection:1.1.0 zone-a eb-k3s-master https://i.imgur.com/ztir9ww.jpg
sleep 10
python -m galileoexperimentsextensions.humandetection.profiling.main pruellerpaul eb-b-controller edgerun/humandetection:1.1.0 zone-b eb-k3s-master https://i.imgur.com/ztir9ww.jpg
sleep 10
python -m galileoexperimentsextensions.humandetection.profiling.main pruellerpaul eb-c-vm-0 edgerun/humandetection:1.1.0 zone-a eb-k3s-master https://i.imgur.com/ztir9ww.jpg
sleep 10

python -m galileoexperimentsextensions.objectdetection.profiling.main pruellerpaul eb-a-controller edgerun/objectdetection:1.1.0 zone-a eb-k3s-master https://i.imgur.com/LpfkZ4D.jpg
sleep 10
python -m galileoexperimentsextensions.objectdetection.profiling.main pruellerpaul eb-b-controller edgerun/objectdetection:1.1.0 zone-b eb-k3s-master https://i.imgur.com/LpfkZ4D.jpg
sleep 10
python -m galileoexperimentsextensions.objectdetection.profiling.main pruellerpaul eb-c-vm-0 edgerun/objectdetection:1.1.0 zone-a eb-k3s-master https://i.imgur.com/LpfkZ4D.jpg
sleep 10

python -m galileoexperimentsextensions.gundetection.profiling.main pruellerpaul eb-a-controller edgerun/gundetection:1.1.0 zone-a eb-k3s-master https://i.imgur.com/ztir9ww.jpg
sleep 10
python -m galileoexperimentsextensions.gundetection.profiling.main pruellerpaul eb-b-controller edgerun/gundetection:1.1.0 zone-b eb-k3s-master https://i.imgur.com/ztir9ww.jpg
sleep 10
python -m galileoexperimentsextensions.gundetection.profiling.main pruellerpaul eb-c-vm-0 edgerun/gundetection:1.1.0 zone-a eb-k3s-master https://i.imgur.com/ztir9ww.jpg