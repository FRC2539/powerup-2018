from .logitechdualshock import LogitechDualShock
from . import logicalaxes

from custom.config import Config

from commands.drivetrain.drivecommand import DriveCommand
from commands.resetcommand import ResetCommand
from commands.climbhook.movehookcommand import movehookCommand
from commands.winch.winchcommand import WinchCommand
from commands.intake.intakecommand import IntakeCommand
from commands.intake.outakecommand import OutakeCommand

def init():
    '''
    Declare all controllers, assign axes to logical axes, and trigger
    commands on various button events. Available event types are:
        - whenPressed
        - whileHeld: cancelled when the button is released
        - whenReleased
        - toggleWhenPressed: start on first press, cancel on next
        - cancelWhenPressed: good for commands started with a different button
    '''

    mainController = LogitechDualShock(0)

    logicalaxes.driveX = mainController.LeftX
    logicalaxes.driveY = mainController.LeftY
    logicalaxes.driveRotate = mainController.RightX

    mainController.Back.whenPressed(ResetCommand())
    mainController.X.toggleWhenPressed(DriveCommand(Config('DriveTrain/preciseSpeed')))
    mainController.A.whileHeld(movehookCommand(-0.3))
    mainController.B.whileHeld(movehookCommand(0.3))
    mainController.Y.whileHeld(WinchCommand(-1))
    mainController.RightTrigger.toggleWhenPressed(OutakeCommand(-1))
    mainController.RightBumper.toggleWhenPressed(IntakeCommand(1))


    '''backupController = LogitechDualShock(1)

    backupController.Back.whenPressed(ResetCommand())
    mainController.X.toggleWhenPressed(DriveCommand(Config('DriveTrain/preciseSpeed')))'''
