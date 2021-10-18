#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
class NumberCounter:
      
      def __init__(self):
          self.ss = " "
          
          #Create dictionary of points with A,B,C tablet
          self.thisdict = {
             "A": [-1.2, 0.87, 1],
             "B": [-1.34, -0.28, 1],
             "C": [-1.11, -1.38, 1],
             "D": [-0.18,-1.46 , 1],
             "E": [-0.10,-0.41, 1],
             "F": [-0.03, 0.78, 1],
             "G": [1, 0.78, 1],
             "H": [0.97,-0.32, 1],
             "I": [1.07,-1.39, 1],
             "HOME":[-1.82,-0.53,1]
           }
          self.number_subscriber = rospy.Subscriber("chatter", String, self.callback)
          self.client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
          rospy.loginfo("Waiting for server")
          self.client.wait_for_server()          
          rospy.loginfo("Connected")
          
      def callback(self, data):
          rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
          self.ss= data.data
          try:
                point = self.thisdict[self.ss]
                print (point)
                self.move_goal_pose(point) 
          except:
	          rospy.logwarn("Exception found")
	          point = [0,0,1] 
        
          
          
          
      def move_goal_pose(self,point):
            rospy.loginfo("Moving to Table name %s", self.ss)
            
   
            goal = MoveBaseGoal()
            goal.target_pose.header.frame_id = "map"
            goal.target_pose.header.stamp = rospy.Time.now()
            goal.target_pose.pose.position.x = point[0]
            goal.target_pose.pose.position.y = point[1]
            goal.target_pose.pose.orientation.w = point[2]

            self.client.send_goal(goal)
            
                 
if __name__ == '__main__':
          rospy.init_node('move_table', anonymous=True)
          NumberCounter()    
          rospy.spin()
