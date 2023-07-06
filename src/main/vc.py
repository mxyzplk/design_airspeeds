import numpy as np
import aircraft
import standard_atmosphere


class Vc:
    def __init__(self):

        self.ac = aircraft.Aircraft()
        self.altitudes = np.empty(int(self.ac.ceiling_f00) + 1)
        self.vc = np.empty(int(self.ac.ceiling_f00) + 1, 4)   # VC given in Calibrated airspeed

        Vc.get_vc(self)

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

    def check_vc(self):
        pass