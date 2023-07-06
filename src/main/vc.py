import numpy as np
import aircraft
import standard_atmosphere
from common_functions import knots2ms
import math


class Vc:
    def __init__(self):

        self.ac = aircraft.Aircraft()
        self.altitudes = np.empty(int(self.ac.ceiling_f00) + 1)
        self.vc = np.empty(int(self.ac.ceiling_f00) + 1, 4)   # VC given in Calibrated airspeed
        self.vc_limit = 0

        Vc.get_vc(self)

        if self.ac.ctype == 23:
            self.check_vc_part_23(self.ac.ws, self.ac.atype)
        else:
            self.check_vc_part_25()

    def get_vc(self):
        for i in range(len(self.altitudes)):
            self.altitudes[i] = i
            speed_cas = standard_atmosphere.Airspeed(self.altitudes[i], float(self.ac.vc[0]), "CAS", self.ac.disa)
            speed_mach = standard_atmosphere.Airspeed(self.altitudes[i], float(self.ac.vc[1]), "Mach", self.ac.disa)

            if self.ac.vc_limitation[0] == 1:
                if float(self.ac.vc_limitation[2]) <= self.altitude[i]:
                    speed_eas = standard_atmosphere.Airspeed(self.altitudes[i], float(self.ac.vc_limitation[1]), "EAS", self.ac.disa)
                else:
                    if speed_cas.mach > float(self.ac.vc[1]):
                        self.vc[i, 0] = speed_mach.eas
                        self.vc[i, 1] = speed_mach.cas
                        self.vc[i, 2] = speed_mach.tas
                        self.vc[i, 3] = speed_mach.mach
                    else:
                        self.vc[i, 0] = speed_eas.eas
                        self.vc[i, 1] = speed_eas.cas
                        self.vc[i, 2] = speed_eas.tas
                        self.vc[i, 3] = speed_eas.mach
            else:
                if speed_cas.mach > float(self.ac.vc[1]):
                    self.vc[i, 0] = speed_mach.eas
                    self.vc[i, 1] = speed_mach.cas
                    self.vc[i, 2] = speed_mach.tas
                    self.vc[i, 3] = speed_mach.mach
                else:
                    self.vc[i, 0] = speed_cas.eas
                    self.vc[i, 1] = speed_cas.cas
                    self.vc[i, 2] = speed_cas.tas
                    self.vc[i, 3] = speed_cas.mach

    def check_vc_part_23(self, ws, atype):

        if atype == 'N' or atype == 'C' atype == 'U':
            if ws <= 20:
                self.vc_limit = knots2ms(33 * math.sqrt(ws))  #CS 23.335(a)(1)(i)
            else:
                factor = (ws - 20) * (28.6 - 33) / (100 - 20) + 33
                self.vc_limit = knots2ms(factor * math.sqrt(ws))  # CS 23.335(a)(2)
        elif atype == 'A':
            if ws <= 20:
                self.vc_limit = knots2ms(36 * math.sqrt(ws))   #CS 23.335(a)(1)(ii)
            else:
                factor = (ws - 20) * (28.6 - 36) / (100 - 20) + 36
                self.vc_limit = knots2ms(factor * math.sqrt(ws))  # CS 23.335(a)(2)


    def check_vc_part_25(self):
        pass