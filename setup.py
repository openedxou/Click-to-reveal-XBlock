"""Setup for c2r XBlock."""

import os
from setuptools import setup



def package_data(pkg, roots):
    """Generic function to find package_data.

    All of the files under each of the `roots` will be declared as package
    data for package `pkg`.

    """
    data = []
    for root in roots:
        for dirname, _, files in os.walk(os.path.join(pkg, root)):
            for fname in files:
                data.append(os.path.relpath(os.path.join(dirname, fname), pkg))

    return {pkg: data}


setup(
    name='c2r-xblock',
    version='0.2',
    description='Click to reveal xblock',   
    license='AGPL v3',         
    packages=[
        'c2r',
    ],
    install_requires=[
        'XBlock',
        'xblock-utils'
    ],
    entry_points={
        'xblock.v1': [
            'c2r = c2r:click2revealxblock',
        ]
    },
    package_data=package_data("c2r", ["static", "public"]),
)
