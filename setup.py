from setuptools import find_packages, setup

setup(
    name='papatya',
    packages=find_packages(include=['papatya']),
    version='0.1.0',
    description='A python library to data manipulation',
    author='https://github.com/bbaransahin',
    license='MIT',
    install_requires=['numpy', 'tqdm'],
    setup_require=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)
