from standard_atmosphere import *
from aircraft import Aircraft
import numpy as np
from scipy.interpolate import interp1d

class Vs:
    def __init__(self, disa):

        self.ac = Aircraft()

        self.altitude_f00 = np.empty(int(self.ac.ceiling_f00))
        self.altitude_fxx = np.array(0, int(self.ac.ceiling_f00))

        self.vs_f00 = np.empty((int(self.ac.ceiling_f00) + 1, 4, 4))  # 4 Design Weights (MTOW, MLW, MZFW, MOW)
        self.vs_fxx = np.empty((2, len(self.ac.clmax_fxx), 4, 4))

        Vs.get_vs_f00(self, disa)
        Vs.get_vs_fxx(self, disa)

    def get_vs_f00(self, disa):

        for i in range(len(self.ac.weights)):                   # Weight loop
            for j in range(len(self.altitude_f00)):             # Altitude Loop
                if i == 0:
                    self.altitude_f00[j] = float(j)             # Setting altitude array

                # The code herein aims to match the correct Vs as clmax = f(airpeed)

                # Initial definitions
                mach_ini = self.ac.clmax_f00[0]

                # Airspeed object. Variables used: Rho
                speed_ini = Airspeed(self.altitude_f00[j], mach_ini, "Mach", disa)

                # Clmax = f(Mach)
                clmax = self.get_clmax(mach_ini, self.ac.clmax_f00)

                # First Vs estimated
                vs_ini = self.calc_vs(clmax, speed_ini.atmos.rho, self.ac.s, self.ac.weights[i])

                # Checking if Vs is equal initial mach
                speed_i = Airspeed(self.altitude_f00[j], vs_ini, "EAS", disa)

                while abs(speed_i.mach - speed_ini.mach) > 0.00001:
                    mach_ini = mach_ini + 0.000001
                    speed_ini = Airspeed(self.altitude_f00[j], mach_ini, "Mach", disa)
                    clmax = self.get_clmax(mach_ini, self.ac.clmax_f00)
                    vs_ini = self.calc_vs(clmax, speed_ini.atmos.rho, self.ac.s, self.ac.weights[i])
                    speed_i = Airspeed(self.altitude_f00[j], vs_ini, "EAS", disa)

                self.vs_f00[j, i, 0] = speed_i.eas
                self.vs_f00[j, i, 1] = speed_i.cas
                self.vs_f00[j, i, 2] = speed_i.tas
                self.vs_f00[j, i, 3] = speed_i.mach

    @staticmethod
    def calc_vs(clmax, rho, s, weight):

        vs = np.sqrt((2 * float(weight)) / (float(rho) * float(s) * float(clmax)))

        return vs

    @staticmethod
    def get_clmax(variable, cl_curve):

        clmax_func = interp1d(cl_curve[0, :], cl_curve[1, :])
        clmax = clmax_func(variable)
        return clmax

    def get_vs_fxx(self, disa):

        for i in range(len(self.ac.weights)):                   # Weight loop
            for j in range(len(self.altitude_fxx)):             # Altitude Loop
                for k in range(len(self.ac.clmax_fxx)):    # Flap Loop
                    atm = Atmosphere(self.altitude_fxx[j], disa)
                    vs = self.calc_vs(self.ac.clmax_fxx[1, k], atm.rho, self.ac.s, self.ac.weights[i])
                    speed = Airspeed(self.altitude_fxx[j], vs, "EAS", disa)
                    self.vs_fxx[j, i, k, 0] = speed.eas
                    self.vs_fxx[j, i, k, 1] = speed.cas
                    self.vs_fxx[j, i, k, 2] = speed.tas
                    self.vs_fxx[j, i, k, 3] = speed.mach
