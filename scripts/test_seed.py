#!/usr/bin/python

import rospy
import __main__
from people_msgs.msg import PositionMeasurement

if __name__ == "__main__":
    rospy.init_node("test_seed")
    seed_publisher = rospy.Publisher("people_tracker_filter", PositionMeasurement)
    while not rospy.is_shutdown() :
        seed = PositionMeasurement()
        seed.header.stamp = rospy.Time.now()
        seed.header.frame_id = "base_link"
        seed.name = "dog"
        seed.pos.x = 1.0
        seed.pos.y = 0.0
        seed.object_id = "dog1"
        seed_publisher.publish(seed)
        raw_input()
        