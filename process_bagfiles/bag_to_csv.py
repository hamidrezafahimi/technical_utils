#!/usr/bin/env python

import rosbag
from cv_bridge import CvBridge
from nav_msgs.msg import Odometry
import pandas as pd
import csv
import argparse
from cv_bridge import CvBridge, CvBridgeError
import cv2 as cv
from pathlib import Path
import numpy as np


parser = argparse.ArgumentParser()
parser.add_argument("file")
args = parser.parse_args()
print(args.file)

bridge = CvBridge()

startIdx = 0
endIdx = 750

initPoint = np.array([29.578, 52.748, 4])
# initPoint = np.array([0, 0, 0])

def getFileName(path):
    k = len(path)-1
    end = k
    for char in path:
        if path[k] != '/':
            if path[k] == '.':
                end = k
            k -= 1
        else:
            break
    return path[k+1:end]

xs = []
ys = []
zs = []
ts = []
cnt = 0
startTime = 0
# odom_cnt = 0

bagFile = args.file
bag = rosbag.Bag(bagFile)
bagName = getFileName(bagFile)
imgDir = bagName+"images/"
img_cnt = 0
Path(imgDir).mkdir(parents=True, exist_ok=True)
# for topic, msg, t in bag.read_messages(topics=['/gazebo/model_states']):
#
#    if topic == '/gazebo/model_states':
       # print("odom: ", odom_cnt)
       # print('---------------------------------------------')
       # print(msg.pose)
       # xs.append(msg.pose[2].position.x)
       # ys.append(msg.pose[2].position.y)
       # zs.append(msg.pose[2].position.z)
       # odom_cnt += 1
for topic, msg, t in bag.read_messages(topics=['/tello/odom', '/tello/camera/image_raw']):
    cnt += 1
    if topic == '/tello/odom' and cnt >= startIdx and cnt <= endIdx:
       xs.append(np.float32(msg.pose.pose.position.x))
       ys.append(np.float32(-msg.pose.pose.position.y))
       zs.append(np.float32(msg.pose.pose.position.z))
       if startTime == 0:
           startTime = msg.header.stamp.to_sec()
       print(msg.header.stamp.to_sec()-startTime)
       ts.append(msg.header.stamp.to_sec()-startTime)


   # if topic == '/tello/camera/image_raw':
   #     image = bridge.imgmsg_to_cv2(msg, "bgr8")
   #     filename = imgDir+str(img_cnt)+".jpg"
   #     cv.imwrite(filename, image)
   #     img_cnt += 1




# theta = 90.0*(np.pi/180)
# xs = np.array(xs)*np.cos(theta) + np.array(ys)*np.sin(theta)
# ys = np.array(ys)*np.cos(theta) - np.array(xs)*np.sin(theta)

zeroDist = initPoint - np.array([xs[0], ys[0], zs[0]])
print(initPoint)
print(np.array([xs[0], ys[0], zs[0]]))
print(zeroDist)


# Xs = np.array(xs) + zeroDist[0]
Xs = -np.array(ys) + zeroDist[0]-10
# Ys = np.array(ys) + zeroDist[1]
Ys = -np.array(xs) + zeroDist[1]-20
# Zs = np.array(zs) + zeroDist[2]
Zs = np.ones(len(xs)) * 4

theta = -15*(np.pi/180)
Xs = np.array(Xs-22)*np.cos(theta) + np.array(Ys-31)*np.sin(theta) +27
Ys = np.array(Ys-31)*np.cos(theta) - np.array(Xs-22)*np.sin(theta)+31

print(Zs[0])
#
xName = 'bagfile_'+bagName+'_x'
yName = 'bagfile_'+bagName+'_y'
zName = 'bagfile_'+bagName+'_z'


# dict = {xName: xs[:-3100], yName: ys[:-3100], zName: zs[:-3100]}
dict = {xName: Xs, yName: Ys, zName: Zs}
#
df = pd.DataFrame(dict)
#
# # saving the dataframe
fileName = 'position_'+bagName+'.csv'

df.to_csv(fileName)
