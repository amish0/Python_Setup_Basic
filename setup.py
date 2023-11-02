from setuptools import setup, find_packages
import os

setup(
    name="mycustompackage",
    version='0.0.2',
    description='how to make setup.py for custom package',
    long_description=open('README.md').read(),
    author='amish Kumar',
    author_email='amishkumar562@gmail.com',
    # install_requires=[
    #     'opencv-python',
    #     'numpy',
    # ],
    include_package_data=True, # https://setuptools.pypa.io/en/stable/userguide/datafiles.html
    install_requires = [
        'opencv-python',
        'numpy>=1.13.3; python_version<"3.7"',
        'numpy>=1.17.0; python_version>="3.7"', # https://github.com/numpy/numpy/pull/13725
        'numpy>=1.17.3; python_version>="3.8"',
        'numpy>=1.19.3; python_version>="3.9"',
        'numpy>=1.21.2; python_version>="3.10"',
        'numpy>=1.19.3; python_version>="3.6" and platform_system=="Linux" and platform_machine=="aarch64"',
        'numpy>=1.21.0; python_version<="3.9" and platform_system=="Darwin" and platform_machine=="arm64"',
        'numpy>=1.21.4; python_version>="3.10" and platform_system=="Darwin"',
        "numpy>=1.23.5; python_version>='3.11'"
    ],
    # packages=find_packages(), # include all packages 
    # packages = ['opencvami'], # include only this package
    packages=['packagecustom_A', 'packagecustom_B'], # include only these packages
)