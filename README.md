# StepAnalysis
This module is dedicated for calculating different Step response analysis factors like  Peak time, Rise time, Settling time, Steady-state value, Overshoot percentage of a specified first or second order system.

# Requirements
1. This module is an extension of Python Control System module and better to use it along with Control System module.
2. Size of Time matrix should be within 5000 to 10000 for better result.
3. Different functions defined in this module requires the step response matrix, time matrix and damping factor of the system. Make sure these are properly available.
4. This module requires 'sympy' module.

# Updates
1. Added support for First order systems.
2. Added support for systems with steady-state error.
3. Bug fixes
 
# Further modification
1. Bug fixes
3. Extension of supporting system orders
2. Flutter based GUI integration

# Installing and importing
1. For Anaconda:
    i) Open Anaconda Prompt.
    ii) Write the following command:
        `pip install stepanalyser`
    iii) import `stepresponse` to your program.
2. For Jupyter Notebook or Google colab:
    i) Add `pip install stepanalyser` before writing the program.
    ii) import `stepresponse` to your program.
3. For system installation;
    i) Write the following command in prompt at proper path:
        `pip install stepanalyser`
    ii) import `stepresponse` to your program.

## For usage example refer `test_example.py` file.
## For more information about the package visit [stepanalyser package](https://pypi.org/project/stepanalyser/).
