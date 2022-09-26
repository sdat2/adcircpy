from adcircpy.outputs.base import SurfaceOutput


class Maxvel(SurfaceOutput):
    _filetype = "maxvel"


class MaximumVelocityTimes(SurfaceOutput):
    _filetype = "time_of_maxvel"
