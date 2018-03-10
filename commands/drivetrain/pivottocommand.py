from .pivotcommand import PivotCommand

import subsystems

class PivotToCommand(PivotCommand):
    '''Pivot to a specified angle using the gyroscope.'''

    def __init__(self, targetDegrees, reverse=False):
        super().__init__(
            targetDegrees,
            reverse,
            'Pivot to %f degrees' % targetDegrees
        )

        self.targetDegrees = targetDegrees
        self.reversed = reverse


    def initialize(self):
        self.distance = subsystems.drivetrain.getAngleTo(self.targetDegrees)
        print("Pivot %s degrees" % self.distance)

        # 0 = Left Side, 1 = Right Side
        self.pivotSide = 0
        if self.distance < 0:
            self.pivotSide = 1

        if self.reversed:
            self.pivotSide = abs(self.pivotSide - 1)

        super().initialize()
