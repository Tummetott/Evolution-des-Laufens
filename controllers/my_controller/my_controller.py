from controller import Robot

robot = Robot()

timestep = int(robot.getBasicTimeStep())

legs = []

legnames = ["left","right"]

for i in range(2):
    legs.append(robot.getDevice(legnames[i]))
    legs[i].setPosition(float('inf'))
    legs[i].setVelocity(0.0)


while robot.step(timestep) != -1:
    leftSpeed = -1
    rightSpeed = 1
    legs[0].setVelocity(leftSpeed)
    legs[1].setVelocity(rightSpeed)