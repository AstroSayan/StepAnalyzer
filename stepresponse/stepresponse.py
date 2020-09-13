"""
This module is dedicated for calculating different Step response analysis factors like 
Peak time, Rise time, Settling time, Steady-state value, Overshoot percentage of a specified 2nd order system.
res = response matrix, time = time matrix and zeta = damping factor

Author: Sayan Das
Email: astrosayan8@gmail.com
Dept. of AEIE
RCC Institute of Information Technology
"""
import numpy as np
from control import *
from math import *

#System representation
def sys(num,den):
  if (len(den)!=3):
    raise ValueError("The system should be of second order.")
  else:
    transfer_function = tf(num,den)
    w =  sqrt(den[2]/den[0])
    zeta = den[1]/(2*w*den[0])
    return [transfer_function, w, zeta]

#Peak time
def peak(res,time,zeta):
  if (zeta==0):
    raise ValueError("Undamped systems do not have any specific Peak time, Rise time, Settling time and steady-state value.")
  elif (zeta>=1):
    raise ValueError("Overdamped or Critically damped systems do not have any Peak time and Settling time.")
  else:
    for i in range(len(res)):
      if (res[i]==np.amax(res)):
        return [time[i],res[i],i]
        
#Rise time
def rise(res,time,zeta):
  if (zeta>=1):
    c = 0
    total = 0
    if (zeta==1):
      for i in range(len(res)):
        if (res[i]>0.94 and res[i]<=0.96):
          total+=time[i]
          c+=1  
      avg = total/c
      return avg
    else:
      for i in range(len(res)):
        if (res[i]>0.89 and res[i]<=0.91):
          total+=time[i]
          c+=1  
      avg = total/c
      return avg  
  else:
    total = 0
    i = 0
    c = 0
    p_t = peak(res, time, zeta)
    ptin = p_t[2]
    while (i<ptin):
      if (res[i]>0.99 and res[i]<=1.01):
        total+=time[i]
        c+=1
      i+=1  
    avg = total/c
    return avg      

#Settling time
def settle(res,time,zeta):
  p_t = peak(res, time, zeta)
  ptin = p_t[2]
  indexes = {}
  p=0
  q=0
  for i in range(ptin,len(res)):
    if (res[i]<1.08):
      p=i
      break
  r = res[p:]
  for i in range(len(r)):
    if (r[i]<0.98 or r[i]>1.02):
      q = p+i
  return time[q+1] 

#Steady-state value
def steady(res,time,zeta):
  if (zeta==0):
    raise ValueError("Undamped systems do not have any specific Peak time, Rise time, Settling time and steady-state value.")
  else:  
    l = len(res)
    r = res[int(7*l/10):]
    for i in range(len(r)-1):
      if (r[i]>0.99 and r[i]<1.01):
        if (abs(r[i+1]-r[i])<0.001):
          s_val = r[i]
          ind = int((7*l/10)+i)
          break
    return [s_val,time[ind]]      

#Overshoot percentage
def overshoot(res,time,zeta):
  p_t = peak(res, time, zeta)
  pamp = p_t[1]
  s_t = steady(res, time, zeta)
  samp = s_t[0]
  ovrsht = ((pamp-samp)/samp)*100
  return ovrsht

#**********************************************************
#Error functions

#peak error
def peak_err(res,time,w,zeta):
  pt = peak(res, time, zeta)
  pr_pt = pt[0]
  th_pt = np.pi/(w*sqrt(1-(zeta**2)))
  err = abs(th_pt-pr_pt)
  p_err = (err*100)/th_pt
  return [th_pt, err, p_err]

#rise error
def rise_err(res,time,w,zeta): 
  pr_rt = rise(res, time, zeta)
  wd = (w*sqrt(1-(zeta**2)))
  theta = atan(wd/(zeta*w))
  th_rt = (np.pi-theta)/wd
  err = abs(th_rt-pr_rt)
  p_err = (err*100)/th_rt
  return [th_rt, err, p_err]

#settle error
def settle_err(res,time,w,zeta):
  pr_st = settle(res, time, zeta)
  th_st = 4/(zeta*w)
  err = abs(th_st-pr_st)
  p_err = (err*100)/th_st
  return [th_st, err, p_err]

#steady-state error at certain time point
def steady_err(res,time,w,zeta,flag):
  sdt = steady(res, time, zeta)
  st = sdt[1]
  if (flag==0):
    time_point = st
    z = sqrt(1-(zeta**2))
    wd = (w*sqrt(1-(zeta**2)))
    phi = acos(zeta)
    p = (zeta*w*time_point)
    err = ((exp(-p))*sin((wd*time_point)+phi))/z
    return err
  elif (flag==1):
    err_list = []
    for i in time:
      time_point = i
      z = sqrt(1-(zeta**2))
      wd = (w*sqrt(1-(zeta**2)))
      phi = acos(zeta)
      p = (zeta*w*time_point)
      err = ((exp(-p))*sin((wd*time_point)+phi))/z 
      err_list.append(err)
    return err_list

#max overshoot error
def overshoot_err(res,time,w,zeta):
  pr_os = (overshoot(res, time, zeta))/100
  th_os = exp(-((np.pi)*zeta)/sqrt(1-(zeta**2)))
  err = abs(th_os-pr_os)
  return [th_os, err]
