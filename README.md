# StepAnalyzer
This module is dedicated for calculating different Step response analysis factors like  Peak time, Rise time, Settling time, Steady-state value, Overshoot percentage of a specified system.

# Requirements
1. This module is an extension of Python Control System module and better to use it along with Control System module.
2. Mandatory inclusion of "Time Matrix" (using numpy.linspace) is required during initialization to avoid errors. Size of Time matrix should be within 5000 to 10000 for better result.
3. Different functions defined in this module requires the step response matrix, time matrix and damping factor of the system. Make sure these are properly available.

# Updates
1. Revamped source code and implementation as "class".
2. Added support for Higher order systems.
3. Added support for systems with offset characteristics.
4. Added support for identifying unstable systems.
5. Added separate error module for domain specific exception messages. 
6. Support for control package, matplotlib and many more all in one module. 
7. Bug fixes
 
# Further modification
1. Bug fixes (if any)
2. Generalizing the module further
3. Kivymd based GUI integration

# Installing and importing
1. For Anaconda:
    i) Open Anaconda Prompt.
    ii) Write the following command:
        `pip install stepanalyzer`
    iii) import `stepanalyzer` to your program.
2. For Jupyter Notebook or Google colab:
    i) Add `!pip install stepanalyzer` before writing the program.
    ii) import `stepanalyzer` to your program.
3. For system installation;
    i) Write the following command in prompt at proper path:
        `pip install stepanalyzer`
    ii) import `stepanalyzer` to your program.

## For usage example refer `test_example.py` file.
## For more information about the package visit [stepanalyzer package](https://pypi.org/project/stepanalyzer/).
