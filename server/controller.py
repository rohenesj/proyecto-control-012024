import numpy as np

def calc(mode,c,params,pwm):
    k = 3/255
    tau = 0.4
    tr, tp, te, zita, omega = params[1], params[2], params[3], params[4], params[5]
    kp, ki, kd = 0, 0, 0
    
    
    if c == "PID":
        p1 = np.sqrt(4*(omega**2)*(zita**2 + tau -1 + 0j)-(4*omega*zita)+ 1)
        a = np.real(-1*(p1 - 2*omega*zita + 1)/(2*(omega**2)))
        b = np.real((p1 + 2*omega*zita - 1)/(2*(omega**2)))
        kc = (omega**2)/k
        kp = round(kc*(a+b),3)
        ki = round(kc,3)
        kd = round(a*b*kc,3)
        dataJson = {"mode": mode, "mp": params[0], "tr": round(tr,3), "tp": round(tp,3), "te": round(te,3), "kp": kp, "ki": ki, "kd": kd, "c": c, "pwm": pwm, "omega":round(omega,3), "zita":round(zita,3)}
        return dataJson
    elif c == "PI":
        kp = round((2*zita*omega*tau -1)/k,3)
        ki = round((tau* omega**2)/k,3)
        dataJson = {"mode": mode, "mp": params[0], "tr": round(tr,3), "tp": round(tp,3), "te": round(te,3), "kp": kp, "ki": ki, "kd": kd, "c": c, "pwm": pwm, "omega":round(omega,3), "zita":round(zita,3)}
        return dataJson
    elif c == "PD":
        kp = round(4/k,3)
        kd = round((te - tau)/k,3)
        tp = te
        tr = te*(3/5)
        dataJson = {"mode": mode, "mp": params[0], "tr": round(tr,3), "tp": round(tp,3), "te": round(te,3), "kp": kp, "ki": ki, "kd": kd, "c": c, "pwm": pwm, "omega":round(omega,3), "zita":round(zita,3)}
        return dataJson
    elif c == "ID":
        kd = round((1/k)*((1/(2*zita*omega)) - tau),3)
        ki = round(((omega**2)/k)*(k*kd + tau),3)
        dataJson = {"mode": mode, "mp": params[0], "tr": round(tr,3), "tp": round(tp,3), "te": round(te,3), "kp": kp, "ki": ki, "kd": kd, "c": c, "pwm": pwm, "omega":round(omega,3), "zita":round(zita,3)}
        return dataJson
    elif c == "P":
        kp = round((1/k)*(((5*tau)/(te))-1),3)
        tp = te
        tr = te*(3/5)
        dataJson = {"mode": mode, "mp": params[0], "tr": round(tr,3), "tp": round(tp,3), "te": round(te,3), "kp": kp, "ki": ki, "kd": kd, "c": c, "pwm": pwm, "omega":round(omega,3), "zita":round(zita,3)}
        return dataJson
    elif c == "I":
        ki = round(((tau*(omega**2))-1)/k,3)
        dataJson = {"mode": mode, "mp": params[0], "tr": round(tr,3), "tp": round(tp,3), "te": round(te,3), "kp": kp, "ki": ki, "kd": kd, "c": c, "pwm": pwm, "omega":round(omega,3), "zita":round(zita,3)}
        return dataJson
    elif c == "D":
        kd = round((1/k)*((te/5)-tau),3)
        tp = te
        tr = te*(3/5)
        dataJson = {"mode": mode, "mp": params[0], "tr": round(tr,3), "tp": round(tp,3), "te": round(te,3), "kp": kp, "ki": ki, "kd": kd, "c": c, "pwm": pwm, "omega":round(omega,3), "zita":round(zita,3)}
        return dataJson
    else:
        return "error"

