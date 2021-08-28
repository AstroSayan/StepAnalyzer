"""
This supporting module is dedicated for creating system object of a given system.

Author: Sayan Das
Email: astrosayan8@gmail.com
Dept. of AEIE
RCC Institute of Information Technology
"""

from control import *
from math import *
import matplotlib.pyplot as plt
from errors import *


class sys:

    def __init__(self, num, den):
        self.num = num
        self.den = den
        self.order = len(den) - 1
        self.omega = None
        self.zeta = None
        self.type = None
        self.tf = None
        self.tfprint = None
        self.stable = None
        if len(self.num) > len(self.den):
            raise SystemError(
                f"Invalid System. Order of numerator {len(self.num) - 1} is greater than the order of denominator {len(self.den) - 1}.")

    def transfer_function(self):
        self.tf = tf(self.num, self.den)
        gm, pm, wg, wp = margin(self.tf)
        if (gm < 0 and pm < 0) and gm > pm:
            self.stable = "Unstable"
            raise StabilityError("The system is unstable!")
        elif gm == pm or (gm == 0 and pm == 0):
            self.stable = "Marginally Stable"
        else:
            self.stable = "Stable"
        return self.tf

    def steadystate(self):
        if self.order == 2:
            self.properties()
            if self.type == "Undamped":
                return "Undamped systems don't have steady-state value."
            else:
                steadyStateVal = dcgain(self.tf)
                return steadyStateVal
        else:
            steadyStateVal = dcgain(self.tf)
            return steadyStateVal

    def properties(self):
        if self.order == 2:
            self.omega = round(sqrt(self.den[2] / self.den[0]), 1)
            self.zeta = round(self.den[1] / (2 * self.omega * self.den[0]), 2)
            if self.zeta == 0:
                self.type = "Undamped"
            elif self.zeta > 1:
                self.type = "Overdamped"
            elif self.zeta == 1:
                self.type = "Critically damped"
            elif self.zeta < 1:
                self.type = "Underdamped"
            return [self.omega, self.zeta]
        else:
            raise PropertyError("System is not of 2nd order.")

    def stepResponse(self, *args, **kwargs):
        t, y = step_response(self.transfer_function(), *args, **kwargs)
        return y, t

    def displayStepResp(self, *args, **kwargs):
        y, t = self.stepResponse(*args, **kwargs)
        plt.plot(t, y)
        plt.grid()
        plt.xlabel("Time (s)")
        plt.ylabel("Amplitude")
        plt.title("Step Response")
        plt.show()

    def getOrder(self):
        return self.order

    def getType(self):
        return self.type

    def omze(self):
        return [self.omega, self.zeta]

    def getStability(self):
        return self.stable

    def getTfprint(self):
        return self.tfprint
