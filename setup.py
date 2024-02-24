from setuptools import setup, find_packages

setup(
    name="mypackage",
    version="0.0.1",
    packages=find_packages(exclude=['tests*']),
    description=open("readme.MD").read()
)