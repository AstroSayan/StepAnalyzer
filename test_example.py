# -*- coding: utf-8 -*-
"""test_example.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GsrNWB_G81rEuf3IHw8egb-sCckt4szy
"""

!pip install control

!pip install -i https://test.pypi.org/simple/ stepanalyser==0.0.1

from control import *         #importing control system library
from stepresponse import *    #importing stepresponse module

t = np.linspace(0,8,10000)    #Creating a time matrix of size 10000 for better result
g = tf([0,0,9],[1,2,9])       #Creating the system
t,y = step_response(g,t)      #Obtaining Step response of the system

zt = 0.33                     #Damping factor 'zeta'

[peak_step,peak_amp,index] = peak(y,t,zt)                 #For peak time, format: peak(response_matrix, time_matrix, zeta), output: list(peak_time, peak_value, index)
print("Peak time: {0:.2f} sec".format(peak_step))

rise_step = rise(y,t,zt)                                  #For rise time, format: rise(response_matrix, time_matrix, zeta), output: rise_time (double)
print("Rise time: {0:.2f} sec".format(rise_step))

settle_step = settle(y,t,zt)                              #For settling time, format: settle(response_matrix, time_matrix, zeta), output: settling_time (double)
print("Settling time: {0:.2f} sec".format(settle_step))

[steady_step, steady_time] = steady(y,t,zt)               #For steady-state value, format: steady(response_matrix, time_matrix, zeta), output: list(steady-state_value, steady-state_time)
print("Steady-state value: {0:.2f} unit(s) at {1:.2f} sec".format(steady_step, steady_time))

ovrsht = overshoot(y,t,zt)                                #For percentage of overshoot, format: overshoot(response_matrix, time_matrix, zeta), output: percentage_overshoot (double)
print("Overshoot percentage: {0:.2f} %".format(ovrsht))


"""
Output of the code ---> (Cross-checked with MATLAB)
--------------------------
Peak time: 1.11 sec
Rise time: 0.68 sec
Settling time: 3.70 sec
Steady-state value: 1.00 unit(s) at 5.60 sec
Overshoot percentage: 32.42 %
"""