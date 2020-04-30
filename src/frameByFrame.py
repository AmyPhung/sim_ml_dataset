#!/usr/bin/env python

import rospy
import rosbag
from sensor_msgs.msg import PointCloud2
from gazebo_msgs.msg import ModelStates
from tf2_msgs.msg import TFMessage
from rosgraph_msgs.msg import Clock



if __name__ == "__main__":

    # Only aspect that is computer-specific
    CATKIN_DIR_LOC = '/home/amy/tractor_sim_ws'

    # Arg 1 is both name of csv and data directory within workspace
    data_dir = '%s/src/sim_ml_dataset/bags' % CATKIN_DIR_LOC

    data_file = '%s/correct.bag' % data_dir

    rospy.init_node('frame_by_frame')

    tf_pub        = rospy.Publisher('/tf',
                                    TFMessage, queue_size=10)
    tf_static_pub = rospy.Publisher('/tf_static',
                                    TFMessage, queue_size=10)
    lidar_pub     = rospy.Publisher('/lidarx_points',
                                    PointCloud2, queue_size=10)
    model_pub     = rospy.Publisher('/gazebo/model_states',
                                    ModelStates, queue_size=10)
    clock_pub     = rospy.Publisher('/clock',
                                    Clock, queue_size=10)



    bag = rosbag.Bag(data_file)
    for topic, msg, t in bag.read_messages(topics=['/tf',
                                                   '/tf_static',
                                                   '/lidarx_points',
                                                   '/gazebo/model_states',
                                                   '/clock']):
        # rospy.loginfo("here")
        if topic == "/tf":
            tf_pub.publish(msg)
        elif topic == "/tf_static":
            tf_static_pub.publish(msg)
        elif topic == "/lidarx_points":
            lidar_pub.publish(msg)

            usr_in = raw_input("Press Enter to continue...")

            if usr_in == "exit":
                break
        elif topic == "/gazebo/model_states":
            model_pub.publish(msg)
        elif topic == "/clock":
            clock_pub.publish(msg)
        else:
            rospy.loginfo("Skipped message")



    bag.close()
