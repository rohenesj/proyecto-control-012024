import matplotlib.pyplot as plt
import control as ct
import numpy as np
import server.plots as plots
# ft = 0.00451 / 1.34s + 1

tau = 0.4
k = 3/255
time = np.linspace(0,6,500)
num = [k]
den = [tau,1]
W = ct.tf(num,den)
print(W)
ref = 255 * np.ones(len(time))

tr, out = ct.forced_response(W,time,ref)
plots.plotting(tr,out,"Respuesta al Impulso","t(s)","PWM","respuestaimp1.png")


### Validcacion de concatenacion de impulsos
im = np.ones(75)
conc = np.concatenate((0*im,0.5*im,0.6*im,im,0.8*im,0.3*im,0.2*im,0.1*im), axis=None)
time2 = np.linspace(0,60,len(conc))
step = np.ones(len(time2))
ref = k * np.ones(len(conc))
tr2, out2 = ct.forced_response(W,time2,conc)
concg = conc * k

plots.plotting2(tr2,concg,out2,"Concatenacion","Respuesta","t(s)","v(V)","variosimp.png")

## Controlador Proporcional


closed_loop = ct.feedback(W,1,-1)

rlocus = ct.root_locus(W)
plots.locus("rootlocus.png")

Kp = 3

opl = ct.series(Kp,W)
csl = ct.feedback(opl,1,-1)
imp = np.ones(len(time)) * k * 0.5

tr3, out3 = ct.forced_response(csl,time,imp)
ref = imp * k
plots.plotting2(tr3,imp,out3,"Concatenacion","Respuesta","t(s)","v(V)","respuestakp.png")
tr31, out31 = ct.forced_response(W,time,imp)
plots.plotting2(tr31,ref,out31,"Concatenacion","Respuesta","t(s)","v(V)","respuestasinkp.png")


## Controlador Integral

Ki = 10

numI = [Ki]
denI = [1,0]

tfI = ct.tf(numI,denI)
PI = ct.parallel(tfI,Kp)
openLoopPI =ct.series(W,PI)
tfPI = ct.feedback(openLoopPI,1,-1)

tr4, out4 = ct.forced_response(tfPI,time,imp)
plots.plotting2(tr4,imp,out4,"Concatenacion","Respuesta","t(s)","v(V)","respuestaPI.png")