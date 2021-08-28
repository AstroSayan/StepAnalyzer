import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="stepanalyzer",
    version="0.3.0",
    license='MIT',
    author="Sayan Das",
    author_email="astrosayan8@gmail.com",
    description="Step Response analyzer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AstroSayan/StepAnalyzer",
    download_url="https://github.com/AstroSayan/StepAnalyzer/archive/refs/tags/v0.3.0.tar.gz",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['numpy',
                      'control', ],
)
