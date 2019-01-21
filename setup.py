
from setuptools import setup, find_packages

setup(
    name="sqlplot",
    author="David Kleiven",
    version=1.0,
    packages=find_packages(),
    scripts=["bin/sqlplot"]
)