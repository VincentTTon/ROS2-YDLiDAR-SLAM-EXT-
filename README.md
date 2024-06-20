# ROS2-YDLiDAR-SLAM-EXT-

This is part of a self driving RC project using ROS2, slam_toolbox, and YDLiDAR running off of a raspberry pi. This portion specifically was located on an external laptop with a second portion located on a raspberry pi 4. The raspberry pi portion can be found here: [https://github.com/VincentTTon/ROS2-YDLiDAR-SLAM-RP4-](https://github.com/VincentTTon/ROS2-YDLiDAR-SLAM-RP4-)


>ros2 launch data_bringup graphic.launch.py

Brings up graphics window and runs slam_toolbox and nav_toolbox

>ros2 launch rf2o_laser_odometry rf2o_laser_odometry.launch.py laser_scan_topic:=scan

Runs laser odometry required for slam_toolbox

