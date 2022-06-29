import numpy as np
import math

from controller import Robot

# L2 (Euclidean) distance
def distance(a, b):
    return np.linalg.norm(a - b)

robot = Robot()
timestep = int(robot.getBasicTimeStep())

legs = []
legNames = ['left','right']
angles = []
angleNames = ['ps_left', 'ps_right']

for i in range(2):
    legs.append(robot.getDevice(legNames[i]))
    legs[i].setPosition(float('inf'))
    legs[i].setVelocity(0.0)
    angles.append(robot.getDevice(angleNames[i]))
    angles[i].enable(timestep)

def readAngles():
    angle_values = [0, 0]
    angle_values[0] = angles[0].getValue() % math.pi
    angle_values[1] = angles[1].getValue() % math.pi
    return angle_values

gps = robot.getDevice('gps')
gps.enable(timestep)

# Don't know why, but we need a step before we can read the startPosition
robot.step(timestep)
startPosition = np.array(gps.getValues())
startTime = robot.getTime()

# First value is the velocity of the left joint
# Second value is the velocity of the right joint
genomVec = [ -1, 1 ]

def elapsedTime():
    return robot.getTime() - startTime

# Our fitness function only calculates the L2 euclidean distance of the robot
# from the start position to the current position
def fitness(genomVec, angleValues, elapsedTime):
    position = np.array(gps.getValues())
    return distance(startPosition, position)

# event loop
while robot.step(timestep) != -1:
    legs[0].setVelocity(genomVec[0])
    legs[1].setVelocity(genomVec[1])

    position = np.array(gps.getValues())
    print(f'distance: {fitness(genomVec, readAngles(), elapsedTime)}')
    # print(f'angles: {readAngles()}')
