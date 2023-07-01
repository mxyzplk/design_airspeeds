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
            speed_eas = standard_atmosphere.Airspeed(self.altitudes[i], self.ac.vc[0], "EAS", 0)
            speed_mach
