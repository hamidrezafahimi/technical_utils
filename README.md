# Technical Utils

A set of go-to programs archived together. The repo contains two types of programs:

* Starting each project, I follow some tutorials and make primary samples before entering the main job. I put all of them here.

* Sometimes I am forced to create simple programs (e.g. reading or writing some special filetypes, plotting specia shapes, dealing with special libraries, etc.) which are pretty simple while taking time to do them again. So, I can store them all in my little *Technical Utils* box. Maybe they work for other people; Why not?

All the folders contain non-related programs and are just classified based on their context. The following workin tree shows what's going on here.

# The Working Tree Explained

## plotting

The directory includes some useful programs for drawing plots in python's *matplotlib* platform.

## ROS/ROS1

### adrone

Here, I've dumped the junk - and of course the successful results - that I collected during my attempts to simulate a quadrotor in the gazebo. Maybe one day I will arrange it so that it takes the form of a respectable document. I don't have time now!

### gi5m

This is how I simply learned Gazebo: My 2019 homeworks following the instructions given in [this course](https://www.youtube.com/playlist?list=PLK0b4e05LnzbHiGDGTgE_FIWpOCvndtYx).

### process_bagfiles

Contains a bunch of python scripts which handle the extraction and plotting of data saved in ROS1 bagfiles.


## ROS/ROS2

Each folder is a ROS2 workspace.

### dev_ws

A Practice of Creating Workspace, Package, Nodes, etc. This is the tutorial is based on what is given in the ROS2 documentaion. 

- [Creating Workspaces](https://docs.ros.org/en/foxy/Tutorials/Beginner-Client-Libraries/Creating-A-Workspace/Creating-A-Workspace.html)

- [Creating Packages](https://docs.ros.org/en/foxy/Tutorials/Beginner-Client-Libraries/Creating-Your-First-ROS2-Package.html)

- [Creating CPP Publisher and Subscriber](https://docs.ros.org/en/foxy/Tutorials/Beginner-Client-Libraries/Writing-A-Simple-Cpp-Publisher-And-Subscriber.html)

- [Creating Python Publisher and Subscriber](https://docs.ros.org/en/foxy/Tutorials/Beginner-Client-Libraries/Writing-A-Simple-Py-Publisher-And-Subscriber.html)

### samples_ws

In this workspace, the useful ROS2 samples are placed to be a simple tutorial and avoid doing ROS2 simple tasks again. For example, the `src/cmd_vel_pub` is a simple velocity commant publisher which can be modified to control robots based on ROS2 platform.

### webots_ws

This is the workspace of my webots projects. I put the initial sample of my webots works here.

#### src/my_package

This is the performed [ros2 official documentation tutorial](https://docs.ros.org/en/foxy/Tutorials/Advanced/Simulators/Webots.html) for simulating robots with ros2. 

#### src/my_mavic

This guy is so useful. It's a native simulation of Mavic 2 Pro, totally stand-alone and independent of ros2-webots installation directories.

## webots

The webots worlds that I've created so far.


