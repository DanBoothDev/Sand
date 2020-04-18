from setuptools import setup, find_packages

install_requires = [
    'gunicorn',
    'WebOb'
]

test_requires = [
    'pytest',
    'pytest-runner'
]

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(name='sand',
      version='0.0.1',
      description='Sand Web Framework',
      install_requires=install_requires,
      tests_require=test_requires,
      long_description=readme,
      license=license,
      packages=find_packages(exclude=('tests', 'docs')))
