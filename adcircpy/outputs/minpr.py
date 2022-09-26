from adcircpy.outputs.base import SurfaceOutput


class Minpr(SurfaceOutput):
    _filetype = "minpr"


class MinimumPressureTimes(SurfaceOutput):
    _filetype = "time_of_minpr"
