#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32

n = 0

def cb(message):
    global n
    n = message.data

if __name__ == '__main__':
    rospy.init_node('twice2')
    sub = rospy.Subscriber('count_down', Int32, cb)
    pub = rospy.Publisher('twice2', Int32, queue_size=1)
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        pub.publish(n)
        rate.sleep()
