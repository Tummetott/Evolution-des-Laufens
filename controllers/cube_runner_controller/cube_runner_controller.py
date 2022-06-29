# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

left_motor = robot.getDevice('left_motor')
right_motor = robot.getDevice('right_motor')

# Initialize motors in order to use velocity control instead of position control.
left_motor.setPosition(float('+inf'))
right_motor.setPosition(float('+inf'))

# Set initial motors velocity.
left_motor.setVelocity(1)
right_motor.setVelocity(0.8)

# Main loop:
while robot.step(timestep) != -1:
    pass
