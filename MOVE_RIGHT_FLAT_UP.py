#!/usr/bin/env python

import rospy
import os
import os.path
import baxter_interface
import baxter_external_devices
from baxter_interface import CHECK_VERSION

def main():
	rospy.init_node('hri_node', anonymous=True)
	rate = rospy.Rate(10) # 10hz
	
	left = baxter_interface.Gripper('left', CHECK_VERSION)
	right = baxter_interface.Gripper('right', CHECK_VERSION)
	
	save_path = '/home/berto/ros_ws/src/articulated_object_manipulation/Log_Files'
	
	fileName = input('Choose the file name: ')
	
	completeName = os.path.join(save_path, "Py_log" + str(fileName) +".txt")
	
	out_file = open(completeName,"w")
	
	out_file.write("=====================================================================================================\n\n")
	out_file.write("Articulated Object Manipulation and Tracking - Log_File_" + str(fileName) + "\n")
	out_file.write("Authors: Riccardo Bertolucci & Roberto Menicatti\n")
	out_file.write("Emails:  richi.bertolucci@gmail.com - roberto.menicatti@hotmail.it\n\n")
	out_file.write("EMARO 2nd year 2015/2016 - Software Architecture Project\n\n")
	out_file.write("=====================================================================================================\n\n")
	
	while not rospy.is_shutdown():
	
		out_file.write("Time: "+ str(rospy.Time.now()) + ": starting left_reach_center\n")

		os.system("rosrun baxter_examples joint_trajectory_file_playback.py -f /home/berto/ros_ws/src/articulated_object_manipulation/actions/left_reach_center.rec")
		
		left.close([])
		
		out_file.write("Time: "+ str(rospy.Time.now()) + ": starting right_reach_right_flat\n")
		
		os.system("rosrun baxter_examples joint_trajectory_file_playback.py -f /home/berto/ros_ws/src/articulated_object_manipulation/actions/right_reach_right_flat.rec")
		
		out_file.write("Time: "+ str(rospy.Time.now()) + ": starting right_pushrotate_right_flat_up\n")
		
		os.system("rosrun baxter_examples joint_trajectory_file_playback.py -f /home/berto/ros_ws/src/articulated_object_manipulation/actions/right_pushrotate_right_flat_up.rec")
		
		out_file.write("Time: "+ str(rospy.Time.now()) + ": starting right_leave_right_up\n")
		
		os.system("rosrun baxter_examples joint_trajectory_file_playback.py -f /home/berto/ros_ws/src/articulated_object_manipulation/actions/right_leave_right_up.rec")
		
		left.open([])
		
		out_file.write("Time: "+ str(rospy.Time.now()) + ": starting left_leave_center\n")
		
		os.system("rosrun baxter_examples joint_trajectory_file_playback.py -f /home/berto/ros_ws/src/articulated_object_manipulation/actions/left_leave_center.rec")

		out_file.close()
		return;
		rospy.spin()


if __name__ == '__main__':
	try:
		main()
	except rospy.ROSInterruptException:
		pass
		
