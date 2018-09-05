from setuptools import setup, find_packages
import os


base_dir = os.path.dirname(__file__)
readme_path = '%s%s' % (''.join(base_dir), 'README.md')
with open(readme_path) as stream:
    long_description = stream.read()

setup(
    name='pyinspector',
    url='https://github.com/omauger/pyinspector',
    author='Ophélie Mauger',
    packages=find_packages(where='.'),
    entry_points={
        'console_scripts': ['pyinspector=pyinspector:main'],
    },
    install_requires=[
        'flake8', 'coverage', 'pylint', 'radon',
        'xenon', 'coloredlogs', 'verboselogs'
    ],
    version='1.2',
    license='MIT',
    description='A module to easely run quality pipeline for python project',
    long_description=long_description,
)
