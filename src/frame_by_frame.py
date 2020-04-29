#!/usr/bin/env python

import rospy
import rosbag
from sensor_msgs.msg import PointCloud2
from gazebo_msgs.msg import ModelStates


# class FrameByFrame()
"""
for message
    if topic is

    def run(self):
        for topic....
            raw_input
            publish
        bag.close()
"""


if __name__ == "__main__":

    # Only aspect that is computer-specific
    CATKIN_DIR_LOC = '/home/amy/tractor_sim_ws'

    # Arg 1 is both name of csv and data directory within workspace
    data_dir = '%s/src/sim_ml_dataset/bags' % CATKIN_DIR_LOC

    data_file = '%s/short.bag' % data_dir

    rospy.init_node('frame_by_frame')

    lidar_pub = rospy.Publisher('/lidarx_points',
                                PointCloud2, queue_size=10)
    model_pub = rospy.Publisher('/gazebo/model_states',
                                ModelStates, queue_size=10)

    bag = rosbag.Bag(data_file)
    for topic, msg, t in bag.read_messages(topics=['/lidarx_points', '/gazebo/model_states']):
        if topic == "/gazebo/model_states":
            model_pub.publish(msg)
        elif topic == "/lidarx_points":
            lidar_pub.publish(msg)
        else:
            print("Skipped message")

        usr_in = raw_input("Press Enter to continue...")
        if usr_in == "exit":
            break

    bag.close()
