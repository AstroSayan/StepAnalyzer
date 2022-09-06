from stepanalyzer import system, step  # importing stepresponse module
import numpy as np

syst = system.sys([9], [1, 2, 9])
tf = syst.transfer_function()
st = syst.steadystate()
wn, zeta = syst.properties()

print("Transfer function: {}".format(tf))
print(f"Order: {syst.getOrder()}\nType: {syst.getType()}\nStability: {syst.getStability()}"
      f"\n")
print("Damped natural frequency (wn): {0:.2f} rad/s & Damping factor (zeta): {1:.2f}".format(wn, zeta))

t = np.linspace(0, 8, 10000)
stepAnal = step.StepAnalyzer([9], [1, 2, 9], t)

# peak time
pv, _, pt = stepAnal.peak()
print("Peak time: {0:.2f} sec\nPeak value: {1:.2f}".format(pt, pv))

# rise time
rt = stepAnal.rise()
print("Rise time: {0:.2f} sec".format(rt))

# rise time
st = stepAnal.settle()
print("Settling time: {0:.2f} sec".format(st))

# overshoot
os = stepAnal.overshoot()
print("Overshoot: {0:.2f}%".format(os))

syst.displayStepResp()
