from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='sand',
    version='0.0.1',
    description='Sand Web Framework',
    long_description=readme,
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
