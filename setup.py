"""setup.py allows the installation of the project by pip."""
import os
import sys
from shutil import rmtree
from setuptools import find_packages, setup, Command
from typing import Dict, List

NAME = "adcircpy"

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

REQUIRED = [
    "appdirs",
    "geopandas",
    "haversine",
    "matplotlib",
    "netCDF4",
    "numpy",
    "pandas",
    "paramiko",
    "pooch",
    "psutil",
    "pyproj>=2.6",
    "requests",
    "scipy",
    "shapely",
    "stormevents>=1.4.0",
    "utm",
    "isort",
    "oitnb",
    "pytest",
    "pytest-cov",
    "pytest-mock",
    "pytest-socket",
    "pytest-xdist",
    "m2r2",
    "sphinx",
    "sphinx",
    "sphinxcontrib-programoutput",
    "sphinxcontrib-bibtex",
]

here = os.path.abspath(os.path.dirname(__file__))


class UploadCommand(Command):
    """Support setup.py upload."""

    description = "Build and publish the package."
    user_options: List = []

    @staticmethod
    def status(s):
        """Print things in bold."""
        print("\033[1m{0}\033[0m".format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        """Publish package to PyPI."""
        try:
            self.status("Removing previous builds…")
            rmtree(os.path.join(here, "dist"))
        except OSError:
            pass

        self.status("Building Source and Wheel (universal) distribution…")
        os.system("{0} setup.py sdist bdist_wheel --universal".format(sys.executable))

        self.status("Uploading the package to PyPI via Twine…")
        os.system("twine upload dist/*")

        self.status("Pushing git tags…")
        os.system("git tag v{0}".format("0.0.1"))
        os.system("git push --tags")

        sys.exit()


setup(
    name=NAME,
    version="0.0.1",
    author="zachary.burnett",
    author_email="zachary.burnett@noaa.gov",
    description="ADCIRCpy",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=str("https://github.com/sdat2/" + NAME),
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    include_package_data=True,
    install_requires=REQUIRED,
    license="GPL-3.0-or-later",
    # test_suite=str(NAME +".tests.test_all.suite"),
    # setup_requires=["pytest-runner"],
    # package_dir={"": NAME},
    tests_require=["pytest", "pooch"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">3.6",
    cmdclass={
        "upload": UploadCommand,
    },
)
