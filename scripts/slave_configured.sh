#!/bin/bash

# PREPARE SLAVE NODE
apt install python3-mpi4py -y

pip3 install ipyparallel

pip3 install numpy fiona shapely rtree pyogrio pyproj networkx matplotlib geopandas osmnx scikit-learn imageio ipywidgets
