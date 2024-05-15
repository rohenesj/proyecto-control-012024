import numpy as np
import control as ct
import plots as plots
import json

def make():
    params = json.load(open('server/controllerData.json'))

    k = 1.17
    tau = 1.34

    kp = float(params["kp"])
    ki = float(params["ki"])
    kd = float(params["kd"])

    time = np.linspace(0,6,500)

    num = [k]
    den = [tau, 1]
    W = ct.tf(num,den)

    kpt = ct.tf([kp],[1])
    kit = ct.tf([ki],[1,0])
    kdt = ct.tf([kd,0],[1])
    ct1 = ct.parallel(kpt,kit)
    ctr = ct.parallel(ct1,kdt)
    optf = ct.series(ctr,W)
    cltf = ct.feedback(optf,1,-1)

    tr, out = ct.step_response(cltf,time)
    plots.plotting(tr,out,"Respuesta PID","t(s)","v(V)","server/static/respuestaActual.png")