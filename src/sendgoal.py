#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import PoseStamped
from tf.transformations import quaternion_from_euler

def send_goal():
    rospy.init_node('send_goal', anonymous=True)
    goal_publisher = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=10)
    
    # Give time for subscribers to connect
    rospy.sleep(2)
    
    # User inputs for coordinates and orientation
    x = float(input("Enter the x coordinate: "))
    y = float(input("Enter the y coordinate: "))
    orientation_deg = float(input("Enter the orientation angle (in degrees): "))
    
    # Convert degrees to radians
    orientation_rad = orientation_deg * (3.14159265359 / 180.0)
    
    # Convert Euler angles (roll, pitch, yaw) to quaternion
    quaternion = quaternion_from_euler(0, 0, orientation_rad)
    
    goal = PoseStamped()
    goal.header.frame_id = "map"  # Frame of reference for the goal
    goal.header.stamp = rospy.Time.now()
    
    # Set the position coordinates (x, y, z)
    goal.pose.position.x = x
    goal.pose.position.y = y
    goal.pose.position.z = 0.0
    
    # Set the orientation using the quaternion (x, y, z, w)
    goal.pose.orientation.x = quaternion[0]
    goal.pose.orientation.y = quaternion[1]
    goal.pose.orientation.z = quaternion[2]
    goal.pose.orientation.w = quaternion[3]
    
    rospy.loginfo("Publishing goal position to move_base...")
    goal_publisher.publish(goal)
    rospy.loginfo("Goal published!")

    rospy.spin()

if __name__ == '__main__':
    try:
        send_goal()
    except rospy.ROSInterruptException:
        pass