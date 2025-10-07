#!/usr/bin/env python3
#### used to visualize customized gemini2 camera and mount in rviz
# To view the gemini2 camera and mount in rviz, in gemini2_with_mount.urdf.xacro
# - use the robot with <robot xmlns:xacro="http://ros.org/wiki/xacro"> at the top of the file
# - add  <xacro:gemini2_with_mount /> at the second last line of the 

from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os
from launch_param_builder import load_xacro
from pathlib import Path

def generate_launch_description():
    xacro_file =Path(get_package_share_directory('xarm_description')) / 'urdf' / 'camera' / 'gemini2_with_mount.urdf.xacro'

    robot_desc = load_xacro(xacro_file)

    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            output='screen',
            name='robot_state_publisher',
            parameters=[{'robot_description': robot_desc}]
        ),
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            name='joint_state_publisher_gui'
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            arguments=['-d', 'path_to_rviz_config.rviz']
        )
    ])
