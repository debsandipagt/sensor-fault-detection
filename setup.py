"""
# This will automatically include all packages (directories containing an __init__.py file) in the source directory. 
# It ensures that all relevant Python modules are included when the package is built.
"""
from setuptools import find_packages, setup
setup(
    name='src',
    version='0.0.1',
    author='Sandip Deb',
    auther_email='debsandip.agt@gmail.com',
    packages=find_packages(), 
    install_requires = [],
)