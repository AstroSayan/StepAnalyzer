import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="stepanalyser", 
    version="0.1.1",
    author="Sayan Das",
    author_email="astrosayan8@gmail.com",
    description="Step response analyser",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AstroSayan/StepAnalysis",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['numpy',
                      'control'],
)
