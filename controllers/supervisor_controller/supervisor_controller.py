from controller import Supervisor
import os
import sys
import numpy as np

MAX_TIME = 20

supervisor = Supervisor()
cube_runner = supervisor.getFromDef("cube_runner")

start_position = np.array(cube_runner.getPosition())

timestep = int(supervisor.getBasicTimeStep())
supervisor.step(timestep)

# L2 (Euclidean) distance
def distance(a, b):
    return np.linalg.norm(a - b)

while supervisor.step(timestep) != -1:
    if supervisor.getTime() > MAX_TIME:
        pos = cube_runner.getPosition()
        print(distance(start_position, pos))
        break
