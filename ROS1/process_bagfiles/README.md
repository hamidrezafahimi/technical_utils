

# processImageBags

How I ran the `processImageBags.py` on ubuntu 20.04:

## Setup:

```
source /opt/ros/noetic/setup.bash

export PATH=~/anaconda3/bin:$PATH

source ~/anaconda3/etc/profile.d/conda.sh

conda activate tello3
# tello3 is a conda environment with python 3.6

# Then, installing packages:

conda install -c conda-forge ros-rospy

conda install -c conda-forge opencv 

... to be completed
```