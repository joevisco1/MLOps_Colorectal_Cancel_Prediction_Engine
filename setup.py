from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="MLOPS_CORR_CANCER",
    version="0.1",
    author="jvisco",
    packages=find_packages(),
    install_requires = requirements,
)