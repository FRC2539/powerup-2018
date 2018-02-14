from wpilib.command.command import Command

import subsystems

class DefaultCommand(Command):

    def __init__(self):
        super().__init__('Default for Elevator')

        self.requires(subsystems.elevator)
