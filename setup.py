from setuptools import setup, find_packages

requires = [
    'gunicorn',
    'WebOb'
]


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='sand',
    version='0.0.1',
    description='Sand Web Framework',
    install_requires=requires,
    long_description=readme,
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
