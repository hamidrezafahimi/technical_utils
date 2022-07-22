#!/usr/bin/env python

import csv
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("file")
args = parser.parse_args()
print(args.file)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


maxXs = -1e6
minXs = 1e6
maxYs = -1e6
minYs = 1e6
maxZs = -1e6
minZs = 1e6

# ax.plot3D([2.75, 3.75, 3.75, 2.75, 2.75], [-5, -5, -5, -5, -5] , [8, 8, 9.5, 9.5, 8], 'r')


fileName = args.file

if fileName == "all":
    all = [
    'position_2020-11-21-19-23-45.csv',
    'position_2020-11-21-19-34-25.csv', #ha
     # 'position_2020-11-21-15-35-25.csv', #na
     'position_2020-11-21-19-41-55.csv', #na
    # 'position_2020-11-21-18-32-28.csv' , #na
    'position_2020-11-21-19-45-02.csv', #ha ?
    'position_2020-11-21-18-56-02.csv' , #ha
    # 'position_2020-11-21-19-50-38.csv', # na
    # 'position_2020-11-21-19-13-39.csv' , na
     # 'position_2020-11-21-19-57-03.csv' #hA
     ]

    # NOTE: The Filed Test: 'position_2020-11-21-19-50-38.csv'
else:
    all = [fileName]

for fileName in all:
    print(fileName)
    xs = []
    ys = []
    zs = []
    with open(fileName, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)

        for k, row in enumerate(data):

            if k == 0:
                continue

            xs.append(float(row[1]))
            ys.append(float(row[2]))
            zs.append(float(row[3]))
            if k == 19200:
                ax.scatter(xs[k-1], ys[k-1], zs[k-1], color=(1,0,0), marker="x")

        print(len(xs))
        ax.plot3D(np.array(xs), np.array(ys), np.array(zs), 'blue')

        if maxXs < max(xs):
            maxXs = max(xs)
        if maxYs < max(ys):
            maxYs = max(ys)
        if maxZs < max(zs):
            maxZs = max(zs)
        if minXs > min(xs):
            minXs = min(xs)
        if minYs > min(ys):
            minYs = min(ys)
        if minZs > min(zs):
            minZs = min(zs)

midPoint = [(maxXs+minXs)/2, (maxYs+minYs)/2, (maxZs+minZs)/2]
maxDist = max((maxXs-minXs), (maxYs-minYs), (maxZs-minZs))
ax.set_xlim(midPoint[0]-(maxDist/2), midPoint[0]+(maxDist/2))
ax.set_ylim(midPoint[1]-(maxDist/2), midPoint[1]+(maxDist/2))
ax.set_zlim(midPoint[2]-(maxDist/2), midPoint[2]+(maxDist/2))

ax.set_xlabel("x (m)")
ax.set_ylabel("y (m)")
ax.set_zlabel("z (m)")

# plt.axis('off')

# plt.savefig(figName)
plt.show()
