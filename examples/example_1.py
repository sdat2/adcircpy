"""ADCIRC

Usage::
    python examples/example_1.py

"""
import os
from datetime import datetime, timedelta
from pathlib import Path
import shutil
import warnings

from adcircpy import AdcircMesh, AdcircRun, Tides
from adcircpy.utilities import download_mesh


def mkdir(dir):
    if not os.path.exists(dir):
        os.mkdir(dir)


DATA_DIRECTORY = Path(__file__).parent.absolute() / "data"
mkdir(DATA_DIRECTORY)
mkdir(DATA_DIRECTORY / "input")
mkdir(DATA_DIRECTORY / "output")
INPUT_DIRECTORY = DATA_DIRECTORY / "input" / "shinnecock"
mkdir(INPUT_DIRECTORY)
OUTPUT_DIRECTORY = DATA_DIRECTORY / "output" / "example_1"
mkdir(OUTPUT_DIRECTORY)
MESH_DIRECTORY = INPUT_DIRECTORY  # / "shinnecock"


download_mesh(
    url="https://www.dropbox.com/s/1wk91r67cacf132/NetCDF_shinnecock_inlet.tar.bz2?dl=1",
    directory=MESH_DIRECTORY,
    known_hash="99d764541983bfee60d4176af48ed803d427dea61243fa22d3f4003ebcec98f4",
)

# open mesh file
mesh = AdcircMesh.open(MESH_DIRECTORY / "fort.14", crs=4326)

# initialize tidal forcing and constituents
tidal_forcing = Tides()
tidal_forcing.use_constituent("M2")
tidal_forcing.use_constituent("N2")
tidal_forcing.use_constituent("S2")
tidal_forcing.use_constituent("K1")
tidal_forcing.use_constituent("O1")
mesh.add_forcing(tidal_forcing)

# set simulation dates
duration = timedelta(days=5)
start_date = datetime(2015, 12, 14)
end_date = start_date + duration

# instantiate driver object
driver = AdcircRun(mesh, start_date, end_date)

# request outputs
driver.set_elevation_surface_output(sampling_rate=timedelta(minutes=30))
driver.set_velocity_surface_output(sampling_rate=timedelta(minutes=30))

# override default options so the resulting `fort.15` matches the original Shinnecock test case options
driver.timestep = 6.0
driver.DRAMP = 2.0
driver.TOUTGE = 3.8
driver.TOUTGV = 3.8
driver.smagorinsky = False
driver.horizontal_mixing_coefficient = 5.0
driver.gwce_solution_scheme = "semi-implicit-legacy"

if shutil.which("padcirc") is not None:
    driver.run(OUTPUT_DIRECTORY, overwrite=True)
elif shutil.which("adcirc") is not None:
    driver.run(OUTPUT_DIRECTORY, overwrite=True, nproc=1)
else:
    warnings.warn(
        "ADCIRC binaries were not found in PATH. "
        "ADCIRC will not run. Writing files to disk..."
    )
    driver.write(OUTPUT_DIRECTORY, overwrite=True)
