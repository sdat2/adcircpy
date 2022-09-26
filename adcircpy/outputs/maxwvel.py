from adcircpy.outputs.base import SurfaceOutput


class Maxwvel(SurfaceOutput):
    _filetype = "maxwvel"


class MaximumWindVelocityTimes(SurfaceOutput):
    _filetype = "time_of_maxwvel"
