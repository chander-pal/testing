from setuptools import setup, find_packages

setup(
    name="my_project",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["pyspark==3.2.0", "pytest==6.2.5"],
)
