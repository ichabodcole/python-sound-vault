from setuptools import find_packages, setup

setup(
    name='sound-vault',
    packages=find_packages(),
    version='0.0.1',
    description='A library for cataloging and playing sound files.',
    author='Cole Reed',
    url="",
    python_requires='>=3.10',
    install_requires=['pydub>=0.25.1 ', 'pydantic>=2.6.4'],
)
