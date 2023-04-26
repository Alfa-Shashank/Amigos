#! /usr/bin/env python

import rospy
import sys
import copy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
import actionlib
import math

class Ur5Moveit:

    # Constructor
    def __init__(self):

        rospy.init_node('move_to_goal', anonymous=True)

        
        self._commander = moveit_commander.roscpp_initialize(sys.argv)
        self._robot = moveit_commander.RobotCommander()
        self._scene = moveit_commander.PlanningSceneInterface()
        self.arm_group = moveit_commander.MoveGroupCommander("ur5_arm")
        self.gripper_group = moveit_commander.MoveGroupCommander("gripper")
        self._display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory, queue_size=1)

        self._exectute_trajectory_client = actionlib.SimpleActionClient('execute_trajectory', moveit_msgs.msg.ExecuteTrajectoryAction)
        self._exectute_trajectory_client.wait_for_server()

        self._planning_frame = self.arm_group.get_planning_frame()
        self._eef_link = self.arm_group.get_end_effector_link()
        self._group_names = self._robot.get_group_names()


        rospy.loginfo('\033[94m' + "Planning Group: {}".format(self._planning_frame) + '\033[0m')
        rospy.loginfo('\033[94m' + "End Effector Link: {}".format(self._eef_link) + '\033[0m')
        rospy.loginfo('\033[94m' + "Group Names: {}".format(self._group_names) + '\033[0m')

        rospy.loginfo('\033[94m' + " >>> Ur5Moveit init done." + '\033[0m')

    # def go_to_predefined_pose(self, arg_pose_name):
    #     rospy.loginfo('\033[94m' + "Going to Pose: {}".format(arg_pose_name) + '\033[0m')
    #     self.arm_group.set_named_target(arg_pose_name)
    #     self.arm_group.go(wait=True)
    #     #goal = moveit_msgs.msg.ExecuteTrajectoryGoal()
    #     #goal.trajectory = plan
    #     #self._exectute_trajectory_client.send_goal(goal)
    #     #self._exectute_trajectory_client.wait_for_result()
    #     rospy.loginfo('\033[94m' + "Now at Pose: {}".format(arg_pose_name) + '\033[0m')

    def set_joint_angles(self, arg_list_joint_angles):


        self.arm_group.set_joint_value_target(arg_list_joint_angles)
        flag_plan = self.arm_group.go(wait=True)

        if (flag_plan == True):
            rospy.loginfo('\033[94m' + ">>> set_joint_angles() Success" + '\033[0m')
        else:
            rospy.loginfo('\033[94m' + ">>> set_joint_angles() Failed." + '\033[0m')


    def go_to_pose(self,arg_pose):

        print("go_to_pose called")

        self.arm_group.set_pose_target(arg_pose)

        #self.arm_group.set_joint_value_target(group_variable_values)
        plan = self.arm_group.plan()
        flag_plan = self.arm_group.go(wait=True)  # wait=False for Async Move



        list_joint_values = self.arm_group.get_current_joint_values()
        rospy.loginfo('\033[94m' + ">>> Final Joint Values:" + '\033[0m')
        rospy.loginfo(list_joint_values)

        if (flag_plan == True):
            rospy.loginfo('\033[94m' + ">>> go_to_pose() Success" + '\033[0m')
        else:
            rospy.loginfo('\033[94m' + ">>> go_to_pose() Failed. Solution for Pose not Found." + '\033[0m')

        return flag_plan

    def gripper(self,arg_pose):
        self.gripper_group.set_named_target(arg_pose) 
        self.gripper_group.go(wait=True)
    

    # Destructor
    def __del__(self):
        moveit_commander.roscpp_shutdown()
        rospy.loginfo('\033[94m' + "Object of class Ur5Moveit Deleted." + '\033[0m')


# def main():

#     ur5 = Ur5Moveit()

    
#     while not rospy.is_shutdown():
#         # upRight_pose = [math.radians(2),math.radians(-92),math.radians(95),math.radians(-5),math.radians(3),math.radians(-50)] 
#         upRight_pose = [-1.5100,-2.5514,2.5861,-2.8291,-1.5794,0.0174]      
#         ur5.set_joint_angles(upRight_pose)
#         rospy.sleep(2)
#         # exit()

#     del ur5


# if __name__ == '__main__':
#     main()

