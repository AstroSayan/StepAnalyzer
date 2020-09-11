from setuptools import setup, find_packages

with open('README.rst') as fp:
    long_description = fp.read()

CLASSIFIERS = """
Development Status :: 1 - Alpha
Intended Audience :: Science/Research
Intended Audience :: Developers
License :: OSI Approved :: MIT License
Programming Language :: Python :: 2
Programming Language :: Python :: 2.7
Programming Language :: Python :: 3
Programming Language :: Python :: 3.5
Programming Language :: Python :: 3.6
Programming Language :: Python :: 3.7
Programming Language :: Python :: 3.8
Topic :: Software Development
Topic :: Scientific/Engineering
Operating System :: Microsoft :: Windows
Operating System :: POSIX
Operating System :: Unix
Operating System :: MacOS
"""

setup(
    name='stepanalysis',
    version='0.0.1',
    author='Sayan Das',
    author_email='astrosayan8@gmail.com',
    url='https://github.com/AstroSayan/StepAnalysis',
    description='Step Response Analysis Toolbox',
    long_description=long_description,
    packages=find_packages(),
    classifiers=[f for f in CLASSIFIERS.split('\n') if f],
    install_requires=['control','numpy'],
)
