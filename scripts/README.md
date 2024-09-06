# CyberGIS Cloud Scripts

CyberGIS Cloud uses many scripts to get started. Currently, 'head_start.sh' runs on the head node before the cluster is fully created. It installes necessary packages and starts a Jupyter notebook instance. The 'head_configured.sh' file starts the connection to the cluster. Currently, this file should be run manually on the head node manually. The 'slave_configured.sh' is simply used to install necessary packages on each of the cluster nodes. 'profile_slurm' contains the Slurm/MPI-related configuration files for IPyParallel. The configuration files are kept minimal.
