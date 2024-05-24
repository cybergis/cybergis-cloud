#!/bin/bash

# PREPARE HEAD NODE
apt install subversion -y
sudo -Hiu ubuntu git clone https://github.com/cybergis/cybergis-cloud.git /home/ubuntu/scripts
sudo -Hiu ubuntu mkdir -p /home/ubuntu/.ipython
sudo -Hiu ubuntu mv /home/ubuntu/scripts/profile_slurm /home/ubuntu/.ipython

sudo -Hiu ubuntu mv /home/ubuntu/scripts/default.ipynb /home/ubuntu/default.ipynb
sudo -Hiu ubuntu mv https://raw.githubusercontent.com/cybergis/cybergis-cloud/main/scripts/head_configured.sh /home/ubuntu/start.sh
chmod +x /home/ubuntu/start.sh

apt install python3-mpi4py -y

pip3 install markupsafe==2.0.1 --force-reinstall
pip3 install notebook
pip3 install ipyparallel

pip3 install numpy fiona shapely rtree pyogrio pyproj networkx matplotlib geopandas osmnx scikit-learn imageio ipywidgets

TOKEN=`curl -s -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600"`
PUBLIC_DNS=`curl -s http://169.254.169.254/latest/meta-data/public-hostname -H "X-aws-ec2-metadata-token: $TOKEN"`
sudo -Hiu ubuntu setsid nohup python3 -m notebook --no-browser --port=8888 --ip=$PUBLIC_DNS --NotebookApp.token='' --NotebookApp.password='' --allow-root > /dev/null 2>&1 & disown
