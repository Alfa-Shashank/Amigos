#! /usr/bin/env python


import rospy
import tf2_ros
import roslib
import sys
import tf2_geometry_msgs 
from cv_bridge import CvBridge, CvBridgeError
from geometry_msgs.msg import PoseStamped, PointStamped
from sensor_msgs.msg import Image, PointCloud2, CameraInfo
from tf.transformations import quaternion_from_euler, euler_from_quaternion
from sensor_msgs.msg import Image, PointCloud2, CameraInfo
import cv2
import numpy


class Vision:
	def __init__(self):

		rospy.init_node("show_me",anonymous = True)
		
		self.image = None

		self.tf_buffer = tf2_ros.Buffer(rospy.Duration(1200.0))
		self.tf_listener = tf2_ros.TransformListener(self.tf_buffer)

		#Defining the topics
		self.image_topic = "/camera_link/color/image_raw"
		# self.depth_topic = "/camera/depth/image_raw2"
		# self.camera_frame = "camera_depth_frame2"
		self.camera_topic = "/camera_link/color/camera_info"
		

		rospy.Subscriber(self.image_topic, Image, self.image_cb)

		self.bridge = CvBridge()

		#Getting the camera info
		self.camera_info = rospy.wait_for_message(self.camera_topic, CameraInfo)

		
		rospy.loginfo("constructor passed")



	def image_cb(self, image):
		try:
			#Converting Sensor Image to cv2 Image
			self.image = self.bridge.imgmsg_to_cv2(image, 'bgr8')
			
			
		except CvBridgeError as e:
			print(e)



	def camera_feed(self):
			cv2.imshow('Display',self.image)
			cv2.waitKey(1)


		# print(t)
		
		    


		
		# print("hi")
		
		# cv2.destroyAllWindows()
		
	
	
def main():

	vision = Vision()
		
	while not rospy.is_shutdown():
		vision.camera_feed()
		rospy.sleep(1)
	
	del vision


if __name__ == '__main__':
	main()