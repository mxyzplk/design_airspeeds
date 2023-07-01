import numpy as np
import aircraft
import standard_atmosphere


class Vc:
    def __init__(self):

        self.ac = aircraft.Aircraft()
        self.altitudes = np.empty(int(self.ac.ceiling_f00) + 1)
        self.vc = np.empty(int(self.ac.ceiling_f00) + 1)

        Vc.get_vc(self)

    def get_vc(self):
        for i in range(len(self.altitudes)):
            self.altitudes[i] = i
            speed_eas = standard_atmosphere.Airspeed(self.altitudes[i], float(self.ac.vc[0]), "CAS", self.ac.disa)
            speed_mach = standard_atmosphere.Airspeed(self.altitudes[i], float(self.ac.vc[1]), "Mach", self.ac.disa)
            if speed_eas.mach > float(self.ac.vc[1]):
                self.vc[i] = speed_mach.cas
            else:
                self.vc[i] = speed_eas.cas
