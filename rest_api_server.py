import numpy as np
from fastapi import FastAPI, Header, HTTPException
from fastapi.responses import JSONResponse, FileResponse
from pydantic import BaseModel
from stepanalyzer.errors import SysError, StabilityError, PropertyError, InputError
from stepanalyzer.system import sys
from stepanalyzer.step import StepAnalyzer


class submit_body(BaseModel):
    num: list
    den: list
    time_points: list


app = FastAPI()


@app.get('/sysinfo')
async def sysInfo(numerator: str = Header(None), denominator: str = Header(None)):
    try:
        num = list(map(int, numerator.split(' ')))
        den = list(map(int, denominator.split(' ')))
        syst = sys(num, den)
        _ = syst.transfer_function()
        try:
            props = syst.properties()
            type = syst.getType()
        except PropertyError as e:
            props = ['undefined', 'undefined']
            type = 'undefined'
        st_state = syst.steadystate()
        if np.isinf(st_state):
            st_state = 'infinity'
        content = {
            'tf': syst.getTfprint(),
            'order': syst.getOrder(),
            'type': type,
            'stability': syst.getStability(),
            'wn': props[0],
            'zeta': props[1],
            'steadystate': st_state
        }
        resp = JSONResponse(content=content)
        return resp
    except SysError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except StabilityError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except PropertyError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except InputError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get('/stepanalysis')
async def sysAnalysis(numerator: str = Header(None), denominator: str = Header(None),
                      time_points: str = Header(None)):
    try:
        num = list(map(int, numerator.split(' ')))
        den = list(map(int, denominator.split(' ')))
        t_points = list(map(int, time_points.split(' ')))
        t = np.linspace(t_points[0],
                        t_points[1],
                        t_points[2])
        stepAnal = StepAnalyzer(num, den, t)
        peak = tuple(stepAnal.peak())
        settling = stepAnal.settle()
        try:
            rise = stepAnal.rise()
        except:
            rise = 'Undefined'
        overshoot = stepAnal.overshoot()
        content = {
            'peak': dict(peakTime=peak[2], peakvalue=peak[0]),
            'rise': rise,
            'settling': settling,
            'overshoot': overshoot
        }
        resp = JSONResponse(content=content)
        return resp
    except SysError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except StabilityError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except PropertyError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except InputError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

