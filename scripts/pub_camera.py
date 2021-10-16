#! /usr/bin/env python


import roslib
import rospy
from std_msgs.msg import Header
from std_msgs.msg import String
from sensor_msgs.msg import Image
IMAGE_WIDTH=640
IMAGE_HEIGHT=480

import sys
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')

import os
import cv2
import numpy as np
import time

def publish_image(imgdata):
    image_temp=Image()
    header = Header(stamp=rospy.Time.now())
    header.frame_id = 'map'
    image_temp.height=IMAGE_HEIGHT
    image_temp.width=IMAGE_WIDTH
    image_temp.encoding='rgb8'
    image_temp.data=np.array(imgdata).tobytes()
    #print(imgdata)
    image_temp.is_bigendian=True
    image_temp.header=header
    image_temp.step=IMAGE_WIDTH*3
    image_pub.publish(image_temp)

if __name__ == '__main__':

    rospy.init_node('pub_cv2_camera', anonymous=True)
    image_topic = rospy.get_param('image_topic', '/usb_cam/image_raw')
    image_pub = rospy.Publisher(image_topic, Image, queue_size=1)

    cap=cv2.VideoCapture(0)
    while not rospy.is_shutdown():
        ret,img=cap.read()
        publish_image(img)
        cv2.imshow('img_show',img)
        key=cv2.waitKey(4)
        if key==ord('q'):
            break
    rospy.spin()
