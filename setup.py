from setuptools import setup, find_packages

_version = '0.1'
_packages = find_packages()
_short_description = 'pylint-web2py is a Pylint plugin to help reduce false ' \
    'positives due to web2py implicit imports'

setup(
    name='pylint-web2py',
    url='https://github.com/dsludwig/pylint-web2py',
    author='Derek Ludwig',
    author_email='derek.s.ludwig@gmail.com',
    description=_short_description,
    version=_version,
    packages=_packages,
    install_requires=['pylint<1.0'],
    license='GPLv2',
    keywords='pylint web2py plugin',
)
