#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class MyNode(Node):
    
    def __init__(self):
        super().__init__("first_node")
        self.counter_ = 0
        self.create_timer(1.0, self.timer_callback)
        #self.get_logger().info("Hello from ROS2") 
        #self gets the functionalities of the node class
        #in this tutorial we have run a python executable and in that
        #executable we create a node, do stuff with that node,
        #and then shut down ros2
        
    def timer_callback(self):
        self.get_logger().info("Hello " + str(self.counter_))
        self.counter_ += 1
        
def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    #spin means that the node is going to be kept alive/continue
    #to run indefinitely until the user enters CTRL+C in the terminal
    #All callbacks will run while it is alive
    
    
    rclpy.shutdown()

if __name__ == '__main__':
    main()