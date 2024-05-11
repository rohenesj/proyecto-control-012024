import numpy as np
import json

def calc(mode,c,params,pwm):
    k = 1.17
    tau = 1.3
    tr, tp, te, zita, omega = params[1], params[2], params[3], params[4], params[5]
    kp, ki, kd = 0, 0, 0
    if c == "PID":
        kp = (2*zita - 1)/k
        ki = omega/k
        kd = ((1/omega)-tau)/k
        dataJson = json.dumps({"mode": mode, "mp": params[0], "tr": tr, "tp": tp, "te": te, "kp": kp, "ki": ki, "kd":kd, "c": c, "pwm": pwm}, sort_keys=True)
        return dataJson
    elif c == "PI":
        kp = (2*zita*omega*tau -1)/k
        ki = (tau* omega**2)/k
        dataJson = json.dumps({"mode": mode, "mp": params[0], "tr": tr, "tp": tp, "te": te, "kp": kp, "ki": ki, "kd":kd, "c": c, "pwm": pwm}, sort_keys=True)
        return dataJson
    elif c == "PD":
        kp = 4/k
        kd = (te - tau)/k
        tp = te
        tr = te*(3/5)
        dataJson = json.dumps({"mode": mode, "mp": params[0], "tr": tr, "tp": tp, "te": te, "kp": kp, "ki": ki, "kd":kd, "c": c, "pwm": pwm}, sort_keys=True)
        return dataJson
    elif c == "ID":
        kd = (1/k)*((1/(2*zita*omega)) - tau)
        ki = ((omega**2)/k)*(k*kd + tau)
        dataJson = json.dumps({"mode": mode, "mp": params[0], "tr": tr, "tp": tp, "te": te, "kp": kp, "ki": ki, "kd":kd, "c": c, "pwm": pwm}, sort_keys=True)
        return dataJson
    elif c == "P":
        kp = (1/k)*(((5*tau)/(te))-1)
        tp = te
        tr = te*(3/5)
        dataJson = json.dumps({"mode": mode, "mp": params[0], "tr": tr, "tp": tp, "te": te, "kp": kp, "ki": ki, "kd":kd, "c": c, "pwm": pwm}, sort_keys=True)
        return dataJson
    elif c == "I":
        ki = ((tau*(omega**2))-1)/k
        dataJson = json.dumps({"mode": mode, "mp": params[0], "tr": tr, "tp": tp, "te": te, "kp": kp, "ki": ki, "kd":kd, "c": c, "pwm": pwm}, sort_keys=True)
        return dataJson
    elif c == "D":
        kd = (1/k)*((te/5)-tau)
        tp = te
        tr = te*(3/5)
        dataJson = json.dumps({"mode": mode, "mp": params[0], "tr": tr, "tp": tp, "te": te, "kp": kp, "ki": ki, "kd":kd, "c": c, "pwm": pwm}, sort_keys=True)
        return dataJson
    else:
        return "error"