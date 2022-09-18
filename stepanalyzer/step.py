"""
This module is dedicated for calculating different Step response analysis factors like
Peak time, Rise time, Settling time, Steady-state value, Overshoot percentage of a specified system.

Author: Sayan Das
Email: astrosayan8@gmail.com
Dept. of AEIE
RCC Institute of Information Technology
"""

from .system import *


class StepAnalyzer(sys):

    def __init__(self, num, den, *args, **kwargs):
        super().__init__(num, den)
        self.peakval = None
        self.peaktime = None
        self.peakindex = None
        self.risetime = None
        self.settletime = None
        self.overshootval = None
        self.res, self.time = super().stepResponse(*args, **kwargs)

    def peak(self):
        if super().getOrder() == 2:
            super().properties()
            if super().getType() == "Underdamped":
                self.peakval = max(self.res)
                self.peakindex = np.where(self.res == self.peakval)[0][0]
                self.peaktime = self.time[self.peakindex]
                return self.peakval, self.peakindex, self.peaktime
            else:
                raise SysError(f"{super().getType()} systems don't have any specific Peak value.")
        elif super().getOrder() < 2:
            raise SysError(f"Systems of order {super().getOrder()} don't have Peak value.")
        else:
            self.peakval = max(self.res)
            self.peakindex = self.res.index(self.peakval)
            self.peaktime = self.time[self.peakindex]
            return self.peakval, self.peakindex, self.peaktime

    def rise(self):
        steadyval = super().steadystate()
        counter = 0
        total = 0
        if super().getOrder() == 2:
            super().properties()
            if super().getType() == "Critically damped":
                for i in range(len(self.res)):
                    if 0.94 * steadyval < self.res[i] <= 0.96 * steadyval:
                        total += self.time[i]
                        counter += 1
                    return round(total / counter, 2)
            elif super().getType() == "Overdamped":
                for i in range(len(self.res)):
                    if 0.89 * steadyval < self.res[i] <= 0.91 * steadyval:
                        total += self.time[i]
                        counter += 1
                    return round(total / counter, 2)
            elif super().getType() == "Underdamped":
                self.peak()
                i = 0
                while i < self.peakindex:
                    if 0.99 * steadyval < self.res[i] <= 1.01 * steadyval:
                        total += self.time[i]
                        counter += 1
                    i += 1
                return round(total / counter, 2)
            else:
                raise SysError(f"{super().type} systems don't have any specific Rise time.")
        elif super().getOrder() < 2:
            for i in range(len(self.res)):
                if 0.89 * steadyval < self.res[i] <= 0.90 * steadyval:
                    total += self.time[i]
                    counter += 1
                return round(total / counter, 2)
        else:
            self.peak()
            i = 0
            while i < self.peakindex:
                if 0.89 * steadyval < self.res[i] <= 0.90 * steadyval:
                    total += self.time[i]
                    counter += 1
                i += 1
            return round(total / counter, 2)

    def settle(self):
        steadyval = super().steadystate()
        p = 0
        q = 0
        if super().getOrder() == 2:
            super().properties()
            if super().getType() == "Underdamped":
                self.peak()
                for i in range(self.peakindex, len(self.res)):
                    if self.res[i] < 1.08 * steadyval:
                        p = i
                        break
                reduced_res = self.res[p:]
                for i in range(len(reduced_res)):
                    if reduced_res[i] < 0.98 * steadyval or reduced_res[i] > 1.02 * steadyval:
                        q = p + i
                return self.time[q + 1]
            else:
                raise SysError(f"{super().getType()} systems don't have any specific Settling time.")
        elif super().getOrder() < 2:
            raise SysError(f"Systems of order {super().getOrder()} don't have Settling time.")
        else:
            self.peak()
            for i in range(self.peakindex, len(self.res)):
                if self.res[i] < 1.08 * steadyval:
                    p = i
                    break
            reduced_res = self.res[p:]
            for i in range(len(reduced_res)):
                if reduced_res[i] < 0.98 * steadyval or reduced_res[i] > 1.02 * steadyval:
                    q = p + i
            return self.time[q + 1]

    def overshoot(self):
        self.peak()
        steadyval = super().steadystate()
        self.overshootval = round(((self.peakval - steadyval) / steadyval) * 100, 2)
        return self.overshootval

    def getResponse(self):
        return self.res, self.time
