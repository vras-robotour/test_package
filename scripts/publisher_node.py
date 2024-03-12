#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def publisher():
    rospy.init_node('publisher_node', anonymous=True)
    pub = rospy.Publisher('my_topic', String, queue_size=10)
    rate = rospy.Rate(1)  # Publish message every 1 second
    while not rospy.is_shutdown():
        msg = String()
        msg.data = "Hello, ROS!"
        rospy.loginfo("Publishing: %s", msg.data)
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass
