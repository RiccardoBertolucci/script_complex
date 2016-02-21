#!/usr/bin/env python

import rospy
import os
import baxter_interface
import baxter_external_devices
from baxter_interface import CHECK_VERSION

def main():
	rospy.init_node('hri_node', anonymous=True)
	rate = rospy.Rate(10) # 10hz
	
	left = baxter_interface.Gripper('left', CHECK_VERSION)
	right = baxter_interface.Gripper('right', CHECK_VERSION)
	input("Write something to start the task...")
	
	while not rospy.is_shutdown():
		os.system("rosrun baxter_examples joint_trajectory_file_playback.py -f /home/berto/ros_ws/src/groupProject/actions/reachMiddle.rec")
		
		right.close([])
		
		os.system("rosrun baxter_examples joint_trajectory_file_playback.py -f /home/berto/ros_ws/src/groupProject/actions/reachLeft.rec")
		
		left.close([])
		
		os.system("rosrun baxter_examples joint_trajectory_file_playback.py -f /home/berto/ros_ws/src/groupProject/actions/rotateLeftDown.rec")
		
		left.open([])
		
		os.system("rosrun baxter_examples joint_trajectory_file_playback.py -f /home/berto/ros_ws/src/groupProject/actions/leaveLeft.rec")
		
		right.open([])
		
		os.system("rosrun baxter_examples joint_trajectory_file_playback.py -f /home/berto/ros_ws/src/groupProject/actions/leaveMiddle.rec")
		
		input("Press something to continue...")
		
		rate.sleep()


if __name__ == '__main__':
	try:
		main()
	except rospy.ROSInterruptException:
		pass
