# setup.py
from setuptools import setup

setup(
    name='vulnerable_requests_example',
    version='0.1',
    install_requires=[
        'requests==2.18.4',  # Vulnerable version
    ],
)
