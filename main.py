#! /usr/bin/env python

import move
import rospy
import yolo_check
import geometry_msgs.msg
import tf2_ros
from geometry_msgs.msg import PoseStamped, PointStamped
import tf2_geometry_msgs
import deepSpeech

import pyttsx

engine = pyttsx.init()

engine.setProperty('rate', 130)

engine.setProperty('volume', 1.0)

#initiating/loading ur5_moveit and YOLO
ur5 = move.Ur5Moveit()
# obj_det = yolo_check.Perception()


# #fucntion to convert alphabetical number to integer number

# number_words = {
#     'zero': 0, 
#     'one': 1, 
#     'two': 2, 
#     'three': 3, 
#     'four': 4, 
#     'five': 5, 
#     'six': 6, 
#     'seven': 7, 
#     'eight': 8, 
#     'nine': 9,
#     'ten': 10,
#     'eleven': 11,
#     'twelve': 12,
#     'thirteen': 13,
#     'fourteen': 14,
#     'fifteen': 15,
#     'sixteen': 16,
#     'seventeen': 17,
#     'eighteen': 18,
#     'nineteen': 19,
#     'twenty': 20,
#     'thirty': 30,
#     'forty': 40,
#     'fifty': 50,
#     'sixty': 60,
#     'seventy': 70,
#     'eighty': 80,
#     'ninety': 90,
#     'hundred': 100,
#     'thousand': 1000,
# }

# def word_to_number(words):
#     words_list = words.split()
#     result = 0
#     temp = 0

#     if words == "first":
#         return(1)
#     elif words == "second":
#         return(2)
#     elif words == "third":
#         return(3)
#     elif words == "last" or words == "l" or words == "la":
#         return(-1)
    
#     for word in words_list:
#         if word == 'and':
#             continue
#         elif word == 'minus':
#             result *= -1
#         elif word == 'hundred':
#             temp *= number_words[word]
#         else:
#             temp += number_words[word]
#     result += temp
#     return result

# # word = "eleven"
# # number = wordsto_number(word)
# # print(number)






# #The belwo 2 lines calls the deepSpeech py file to activate dsp1 env and run the dsp-orignal.py script
# d = deepSpeech.dsp()
# d.start()

# command = ""
# with open("/home/shashank/catkin_ws/src/amigos/src/output.txt","r")  as f:
#     command = command +f.readline()
#     command =command.strip()

# if command == "amigos" or command == "amigo":
#     engine.say("Say scan to find objects or say sleep to end")
#     engine.runAndWait()

#     d = deepSpeech.dsp()
#     d.start()
#     print("after executing subprocess")

#     command = ""
#     with open("/home/shashank/catkin_ws/src/amigos/src/output.txt","r")  as f:
#         command = command +f.readline()
#         command =command.strip()
    
#     if command == "scan" or command == "can":
#         engine.say("Scanning objects")
#         engine.runAndWait()

#         print("rotating arm to scan table objects")

#         upRight_pose = [-1.5100,-2.5514,2.5861,-2.8291,-1.5794,0.0174]
#         ur5.set_joint_angles(upRight_pose)
            
        

#         objs_pose_list = obj_det.predict()

#         # x,y,z,obj_count = obj_pose
#         # x = obj_pose.x
#         # y  = obj_pose.y
#         # z = obj_pose.z
#         # print("x,y,z wrt world are")

#         #running recog before only to ask which object, saving time in loading.
#         d = deepSpeech.dsp()
#         d.start()

#         engine.say("choose an object which you want to get")
#         engine.runAndWait()

#         command = ""
#         with open("/home/shashank/catkin_ws/src/amigos/src/output.txt","r")  as f:
#                 command = command +f.readline()
#                 command =command.strip()
        
#         if command != " ":
#                 which_obj = word_to_number(command)
#                 if which_obj == -1: #to get numebr of the last object bcz ever list has obejct count
#                 #     pos = objs_pose_list[0][-1]
#                         x,y,z,obj_count = objs_pose_list[-1]
#                 else:
#                         x,y,z,obj_count = objs_pose_list[which_obj-1]
                
#                 # print(x,y,z)

#                 ur5_pose = geometry_msgs.msg.PoseStamped()
#                 ur5_pose.header.frame_id = "base_link"
#                 ur5_pose.pose.position.x = x
#                 ur5_pose.pose.position.y = y
#                 ur5_pose.pose.position.z = z
#                 ur5_pose.pose.orientation.x = 0.0
#                 ur5_pose.pose.orientation.y = 0.707
#                 ur5_pose.pose.orientation.z = 0.0
#                 ur5_pose.pose.orientation.w = 0.707
#                 print(ur5_pose)
#                 while not rospy.is_shutdown():
#                         flag_plan = ur5.go_to_pose(ur5_pose)
#                         if flag_plan == True:
#                                 break
#                         rospy.sleep(1)






# else:
#     engine.say("command is wrong")
#     engine.runAndWait()


ur5_pose = geometry_msgs.msg.PoseStamped()
ur5_pose.header.frame_id = "world"
ur5_pose.pose.position.x = -0.994801
ur5_pose.pose.position.y = -0.013468
ur5_pose.pose.position.z = 1.014996
ur5_pose.pose.orientation.x = 0.0
ur5_pose.pose.orientation.y = 0.707
ur5_pose.pose.orientation.z = 0.0
ur5_pose.pose.orientation.w = 0.707
print(ur5_pose)
while not rospy.is_shutdown():
                        flag_plan = ur5.go_to_pose(ur5_pose)
                        if flag_plan == True:
                                break
                        rospy.sleep(1)

#     print("executing the command...")
#     upRight_pose = [-1.5100,-2.5514,2.5861,-2.8291,-1.5794,0.0174]
#     ur5.set_joint_angles(upRight_pose)



# while not rospy.is_shutdown():
        # upRight_pose = [math.radians(2),math.radians(-92),math.radians(95),math.radians(-5),math.radians(3),math.radians(-50)] 

        # rospy.sleep(2)
        # exit()
# rospy.sleep(2)

# del ur5

# obj_det = yolo_check.Perception()

# obj_pose = obj_det.predict()
# x = obj_pose.x
# y  = obj_pose.y
# z = obj_pose.z
# print("x,y,z wrt world are")
# print(x,y,z)


# ur5_pose = geometry_msgs.msg.PoseStamped()
# ur5_pose.header.frame_id = "base_link"
# ur5_pose.pose.position.x = 0.5
# ur5_pose.pose.position.y = 0.0
# ur5_pose.pose.position.z = 0.5
# ur5_pose.pose.orientation.x = 0.0
# ur5_pose.pose.orientation.y = 0.0
# ur5_pose.pose.orientation.z = 0.0
# ur5_pose.pose.orientation.w = 1.0


# tf_buffer = tf2_ros.Buffer(rospy.Duration(1200.0))
# tf_listener = tf2_ros.TransformListener(tf_buffer)

# x,y,z = -0.6572657742447967, -0.12061547655747959, 1.6476046690723682
# point_wrt_camera = PointStamped()
# point_wrt_camera.header.frame_id = "world"
# point_wrt_camera.point.x =  x
# point_wrt_camera.point.y =  y
# point_wrt_camera.point.z =  z


# target_frame = "base_link"
# source_frame = "world"
# transform = tf_buffer.lookup_transform(target_frame,source_frame, rospy.Time(0),rospy.Duration(1.0)) 

# base_link_pts = tf2_geometry_msgs.do_transform_point(point_wrt_camera, transform)
# print("pts wrt base_link")
# print(base_link_pts.point)


# ur5_pose = geometry_msgs.msg.PoseStamped()
# ur5_pose.header.frame_id = "world"
# ur5_pose.pose.position.x = x
# ur5_pose.pose.position.y = y
# ur5_pose.pose.position.z = z
# ur5_pose.pose.orientation.x = 0.0
# ur5_pose.pose.orientation.y = 0.0
# ur5_pose.pose.orientation.z = 0.0
# ur5_pose.pose.orientation.w = 1.0
# print(ur5_pose)
# while not rospy.is_shutdown():
#     ur5.go_to_pose(ur5_pose)
#     rospy.sleep(1)




