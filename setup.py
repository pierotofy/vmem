import setuptools
import sys

with open("README.md", "r") as fh:
    long_description = fh.read()

INSTALL_REQUIRES=[]

setuptools.setup(
    name="vmem",
    version="1.0.1",
    author="Piero Toffanin",
    author_email="pt@uav4geo.com",
    description="Cross-platform virtual memory information",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pierotofy/vmem",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    install_requires=INSTALL_REQUIRES
)
