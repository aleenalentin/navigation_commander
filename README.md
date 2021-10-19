# navigation_commander

navigation_commander is a ROS package to command the robot to navigate autonomously to each table for food delivery inside a hotel. Here we use turtlebot 3 waffle_pi gazebo simulation for the demo.

The package comes with a commander node for *move_base* and a GUI to send commands to the command node.

The GUI is typically designed for a hotel room of nine tables. The user can set a table position in the map of the hotel and command the robot to go to a particular table to deliver the food. After delivering the food, the user can command the robot to go to its home position. 

# Prerequisites
* [Ubuntu 20.04 Focal Fossa](https://releases.ubuntu.com/20.04/)
* [PyQt5 ](https://gist.github.com/ujjwal96/1dcd57542bdaf3c9d1b0dd526ccd44ff) 
* [ROS Noetic Ninjemys](http://wiki.ros.org/noetic/Installation)
* [Turtlebot3 Simulation]( https://automaticaddison.com/how-to-launch-the-turtlebot3-simulation-with-ros/)

 
 # How to Build

After installing, clone to a ROS workspace inside src folder and do catkin_make.

```bash
cd ~/catkin_ws/src

git clone https://github.com/aleenalentin/navigation_commander.git

cd ~/catkin_ws

catkin_make
```
# Launching application

You can start the turtlebot 3 simulation, navigation and control GUI using the following launch file



```bash
 roslaunch navi_commander demo.launch

```
# Demo 

Click on the following image to see the demo video


[![Introduction Video](https://img.youtube.com/vi/XMKM8N5_bg8/0.jpg)](https://youtu.be/XMKM8N5_bg8)
# Acknowledgment

*  [Learning Robotics using Python by Lentin Joseph](https://www.amazon.in/Learning-Robotics-Python-Lentin-Joseph/dp/1783287535)
