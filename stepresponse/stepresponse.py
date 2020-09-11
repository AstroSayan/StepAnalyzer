"""
This module is dedicated for calculating different Step response analysis factors like 
Peak time, Rise time, Settling time, Steady-state value, Overshoot percentage of a specified 2nd order system.
res = response matrix, time = time matrix and zeta = damping factor

Author: Sayan Das
Email: astrosayan8@gmail.com
Dept. of AEIE
RCC Institute of Information Technology
"""

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
