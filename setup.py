import  os
from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name = 'Anime-recommender',
    description = 'A simple anime recommender system',
    version = '0.0.1',
    author = 'sachin',
    packages= find_packages(),
    install_requires=requirements,
)