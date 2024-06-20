import os
from pathlib import Path
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.conditions import IfCondition
from launch.conditions import UnlessCondition
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import ThisLaunchFileDir
from launch.actions import ExecuteProcess
from launch.substitutions import LaunchConfiguration, PythonExpression
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()
   
    rf2o = Node(
                package='rf2o_laser_odometry',
                executable='rf2o_laser_odometry_node',
                name='rf2o_laser_odometry',
                output='screen',
                parameters=[{
                    'laser_scan_topic' : '/scan',
                    'odom_topic' : '/odom',
                    'publish_tf' : True,
                    'base_frame_id' : 'base_link',
                    'odom_frame_id' : 'odom',
                    'init_pose_from_topic' : '',
                    'freq' : 10.0}],
            )
    rviz = Node(
                package='rviz2',
                executable='rviz2',
                name='rviz2',
                arguments=['-d'+'/home/vincent/ydlidar_ros2_ws/install/ydlidar_ros2_driver/share/ydlidar_ros2_driver/config/ydlidar.rviz']
                
            )
    
    nav2 = IncludeLaunchDescription(
                PythonLaunchDescriptionSource(
                    "/opt/ros/iron/share/nav2_bringup/launch/navigation_launch.py"
                )

            )
    ld.add_action(nav2)
    ld.add_action(rf2o)
    ld.add_action(rviz)

    return ld
