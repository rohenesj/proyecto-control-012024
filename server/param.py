import numpy as np


def calc (mode, mp, tr, tp, te):
    if mode == "2":
        mp = float(mp) / 100
        tr = float(tr)
        zitaStep1 = (-np.pi/np.log(mp)) ** 2
        zita = 1/(np.sqrt(zitaStep1 + 1))
        omegaStep1 = np.sqrt(1 - (zita**2))
        omega = (np.pi - np.arctan(omegaStep1/zita))/(tr * omegaStep1)
        tp = np.pi / (omegaStep1 * omega)
        te = 4 / (zita * omega)
        return [mp, tr, tp, te, zita, omega]
    elif mode == "3":
        mp = float(mp) / 100
        tp = float(tp)
        zitaStep1 = (-np.pi/np.log(mp)) ** 2
        zita = 1/(np.sqrt(zitaStep1 + 1))
        omegaStep1 = np.sqrt(1 - (zita**2))
        omega = np.pi / (omegaStep1 * tp)
        tr = (np.pi - np.arctan(omegaStep1/zita))/(omega * omegaStep1)
        te = 4 / (zita * omega)
        return [mp, tr, tp, te, zita, omega]
    elif mode == "4":
        mp = float(mp) / 100
        te = float(te)
        zitaStep1 = (-np.pi/np.log(mp)) ** 2
        zita = 1/(np.sqrt(zitaStep1 + 1))
        omegaStep1 = np.sqrt(1 - (zita**2))
        omega = 4 / (zita * te)
        tp = np.pi / (omegaStep1 * omega)
        tr = (np.pi - np.arctan(omegaStep1/zita))/(omega * omegaStep1)
        return [mp, tr, tp, te, zita, omega]
    else:
        return [mode, mp, tr, tp, te]

