#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32

if __name__ == '__main__':
    rospy.init_node('count2')
    pub = rospy.Publisher('count_down', Int32, queue_size=1)
    rate = rospy.Rate(1)
    n = 180
    while not rospy.is_shutdown():
        while ( n > 0):
		n -= 1
       		pub.publish(n)
        	rate.sleep()
	else:
		n = 0
