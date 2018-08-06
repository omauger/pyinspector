from setuptools import setup, find_packages


base_dir = os.path.dirname(__file__)
readme_path = join(base_dir, 'README.md')
with open(readme_path) as stream:
    long_description = stream.read()

setup(
    name='pyquality',
    url='https://github.com/omauger/pyquality',
    author='Ophélie Mauger',
    packages=find_packages(where='.'),
    entry_points={
        'console_scripts': ['pyquality=pyquality:main'],
    },
    install_requires=[
        'flake8', 'coverage', 'pylint', 'radon',
        'xenon', 'coloredlogs', 'verboselogs'
    ],
    version='1.0',
    license='MIT',
    description='A module to easely run quality pipeline for python project',
    loong_description=long_description,
)
