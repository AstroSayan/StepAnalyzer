# -*- coding: utf-8 -*-
"""test_example.ipynb

Automatically generated by Colaboratory.

Author: Sayan Das

Original file is located at
    https://colab.research.google.com/drive/1GsrNWB_G81rEuf3IHw8egb-sCckt4szy
    
Add !pip install control and !pip install stepanalyser==0.1.1 if you are using Google colab or Jupyter notebook    
"""

from control import *           #importing control system library
from stepresponse import *      #importing stepresponse module
import matplotlib.pyplot as plt #importing matplotlib module
g,w,zt=sys([9],[1,2,9])         #Creating the system, format: sys(numerator, denominator), output: list(transfer_function, wn, zeta) 

print("Transfer function: {}".format(g))
print("Damped natural frequency (wn): {0:.2f} rad/s & Damping factor (zeta): {1:.2f}".format(w,zt))

t = np.linspace(0,8,10000)      #Creating a time matrix of size 10000 for better result       
t,y = step_response(g,t)        #Obtaining Step response of the system
                     
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

[th_pt, err, p_err]=peak_err(y,t,w,zt)     #For peak-time error, format: peak_err(response_matrix, time_matrix, wn, zeta), output: list(theoretical peak-time, absolute peak-time error, percentage peak-time error) 
print("Theoretical peak time: {0:.4f} sec. Absolute peak time error: {1:.4f}. Percentage peak time error: {2:.4f} %".format(th_pt, err, p_err))

[th_rt, err1, p_err1]=rise_err(y,t,w,zt)   #For rise-time error, format: rise_err(response_matrix, time_matrix, wn, zeta), output: list(theoretical rise-time, absolute rise-time error, percentage rise-time error)
print("Theoretical rise time: {0:.4f} sec. Absolute rise time error: {1:.4f}. Percentage rise time error: {2:.4f} %".format(th_rt, err1, p_err1))

[th_st, err2, p_err2]=settle_err(y,t,w,zt) #For settling-time error, format: settle_err(response_matrix, time_matrix, wn, zeta), output: list(theoretical settling-time, absolute settling-time error, percentage settling-time error)
print("Theoretical settling time: {0:.4f} sec. Absolute settling time error: {1:.4f}. Percentage settling time error: {2:.4f} %".format(th_st, err2, p_err2))

"""
For steady-state error, format: steady_err(response_matrix, time_matrix, wn, zeta, flag)
**flag can be 0 or 1**
i) when flag = 0,
the function gives steady-state error at infinite time.
ii) when flag = 1,
the function returns an array containing steady-state errors for each time point of time matrix.
"""

err3 = steady_err(y,t,w,zt,0)       #flag = 0    
print("Steady-state error: {0:.4f}".format(err3))

err_list = steady_err(y,t,w,zt,1)   #flag = 1, returns the list. This snippet creates a plot of steady-state error vs. time of the system. Test it in your IDE. 
plt.plot(t,err_list)
plt.grid()
plt.xlabel("time")
plt.ylabel("Steady-state error")
plt.title("Steady-state error vs. time")

[th_ot, err4]=overshoot_err(y,t,w,zt)      #For settling-time error, format: settle_err(response_matrix, time_matrix, wn, zeta), output: list(theoretical overshoot, absolute max overshoot error)            
print("Theoretical max-overshoot: {0:.4f} unit(s). Absolute max-overshoot error: {1:.4f}.".format(th_ot, err4))

"""
Output of the code ---> (Cross-checked with MATLAB)
------------------------------------------------------------------------------------------------------------------------------
Transfer function: 
      9
-------------
s^2 + 2 s + 9

Damped natural frequency (wn): 3.00 rad/s & Damping factor (zeta): 0.33
Peak time: 1.11 sec
Rise time: 0.68 sec
Settling time: 3.70 sec
Steady-state value: 1.00 unit(s) at 5.60 sec
Overshoot percentage: 32.42 %
Theoretical peak time: 1.1107 sec. Absolute peak time error: 0.0002. Percentage peak time error: 0.0189 %
Theoretical rise time: 0.6755 sec. Absolute rise time error: 0.0002. Percentage rise time error: 0.0232 %
Theoretical settling time: 4.0000 sec. Absolute settling time error: 0.2988. Percentage settling time error: 7.4707 %
Steady-state error: -0.0038
Theoretical max-overshoot: 0.3293 unit(s). Absolute max-overshoot error: 0.0051.

<plot>
"""
