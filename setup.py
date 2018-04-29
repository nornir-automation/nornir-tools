#!/usr/bin/env python
from setuptools import setup

with open("requirements.txt", "r") as fs:
    reqs = [r for r in fs.read().splitlines() if (len(r) > 0 and not r.startswith("#"))]

with open("README.md", "r") as fs:
    long_description = fs.read()

__author__ = "dbarrosop@dravetech.com"
__license__ = "Apache License, version 2"

__version__ = "0.0.1"

setup(
    name="brg-tools",
    version=__version__,
    description="Fighting fire with fire",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=__author__,
    url="https://github.com/brigade-automation/brg-tools",
    entry_points={
        "console_scripts": {
            "brg-tools-nw-backup = tools.network.backup.backup:run",
            "brg-tools-nw-get_facts = tools.network.get_facts.get_facts:run",
        }
    },
    include_package_data=True,
    install_requires=reqs,
    packages=["tools"],
    license=__license__,
    test_suite="tests",
    platforms="any",
    classifiers=["Programming Language :: Python :: 3.6"],
)
