#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def callback(msg):
    rospy.loginfo("I heard: %s", msg.data)

def subscriber():
    rospy.init_node('subscriber_node', anonymous=True)
    rospy.Subscriber('my_topic', String, callback)
    rospy.spin()

if __name__ == '__main__':
    subscriber()
