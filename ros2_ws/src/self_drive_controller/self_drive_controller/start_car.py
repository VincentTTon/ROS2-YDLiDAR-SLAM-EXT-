#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
class MyNode(Node):

    def __init__(self):
        super().__init__("Control_Node")
        print("Hello YOU")
        self.get_logger().info("Hello from ROS2") ##Print Statement
        #self.create_timer(1.0,self.timer_callback)
        self.start_pub = self.create_publisher(String, "/chatter",10)
        self.x = input("Enter")
        self.send_command()
    def timer_callback(self):
        self.get_logger().info("Hello")

    def send_command(self):
        msg = String()
        msg.data = "START"
        self.start_pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    print("Hello")

    rclpy.shutdown()


if __name__=='__main__':
    main()