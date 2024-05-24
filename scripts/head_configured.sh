#!/bin/bash

# START HEAD NODE
n=`sudo -Hiu ubuntu sinfo -o '%C' | sed '2q;d' | sed 's:.*/::'`
sudo -Hiu ubuntu ipcluster start --n=$n --profile=slurm
