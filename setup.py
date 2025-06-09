from setuptools import setup, find_packages

setup(
    name="adnan_cnc",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "PyQt5==5.15.4",
        "numpy",
        "shapely",
        "ezdxf"
    ],
)