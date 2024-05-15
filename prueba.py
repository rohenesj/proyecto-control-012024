import numpy as np
import control as ct
import server.plots as plots


omega = 3.66
zita = 0.2154
tau = 1.34

p1 = np.sqrt(4*(omega**2)*(zita**2 + tau -1)-(4*omega*zita)+ 1)
a = -1*(p1 - 2*omega*zita + 1)/(2*(omega**2))
b = (p1 + 2*omega*zita - 1)/(2*(omega**2))
kc = (omega**2)/1.17

kp = kc*(a+b)
ki = kc
kd = a*b*kc

time = np.linspace(0,6,500)

num = [1.17]
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
plots.plotting(tr,out,"Respuesta PID","t(s)","v(V)","respuestaPID.png")


