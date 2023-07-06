#
from standard_atmosphere import Airspeed
import numpy as np
import math


class Va:
    def __init__(self, altitudes, vs, vc, lf, disa):
        # vs and vc given in terms of EAS
        self.va = np.empty((len(vs), 4))
        self.altitudes = np.empty(len(altitudes))
        self.altitudes[:] = altitudes[:]

        self.calc_va(vs, vc, lf, altitudes, disa)

    def calc_va(self, vs, vc, lf, altitudes, disa):

        for i in range(len(vs)):
            self.va[i, 0] = vs[i] * math.sqrt(lf) # 23.335
            if self.va[i, 0] > vc[i]:
                self.va[i, 0] = vc[i]

            speed = Airspeed(altitudes[i], self.va[i, 0], "EAS", disa)
            self.va[i, 0] = speed.eas
            self.va[i, 1] = speed.cas
            self.va[i, 2] = speed.tas
            self.va[i, 3] = speed.mach

