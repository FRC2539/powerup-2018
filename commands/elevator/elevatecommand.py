from wpilib.command import Command

import robot

class ElevateCommand(Command):

    def __init__(self):
        super().__init__('Elevate')

        self.requires(robot.elevator)


    def initialize(self):
        robot.elevator.up()


    def end(self):
        robot.elevator.stop()
