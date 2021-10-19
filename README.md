# navigation_commander
Navigation_Commander is an integration of software packages for performing autonomous navigation. Here we use TURTLEBOT3_MODEL as waffle_pi, simulation world as turtlebot3_world.launch from  turtlebot3_gazebo package and Navigation node as turtlebot3_navigation.launch from turtlebot3_navigation package. First step is to build a GUI to control the robot. Building a GUI that can act as a trigger for the underlying ROS command.Instead of running all the commands on the Terminal, the user can work with GUI buttons. The GUI is typically desinged for a hotel room of nine tables. The user can set a table position in the map of the hotel room and command the robot to go to a particular table to deliver the food. After delivering the food, the user can command the robot to go to its home position. 

# Prerequisites
* [Ubuntu 20.04 Focal Fossa](https://releases.ubuntu.com/20.04/)
* [PyQt5 ](https://gist.github.com/ujjwal96/1dcd57542bdaf3c9d1b0dd526ccd44ff) 
* [ROS Noetic Ninjemys](http://wiki.ros.org/noetic/Installation)
* [Turtlebot3]( https://automaticaddison.com/how-to-launch-the-turtlebot3-simulation-with-ros/)

 
 # How to Build

After installing, you can follow the step to build this project
```bash
git clone https://github.com/aleenalentin/navigation_commander.git

```
open a new terminal and type 
```bash
 roslaunch navi_commander demo.launch

```
# Demo 

Click on the following image to see the video


[![Introduction Video](https://img.youtube.com/vi/XMKM8N5_bg8/0.jpg)](https://youtu.be/XMKM8N5_bg8)
