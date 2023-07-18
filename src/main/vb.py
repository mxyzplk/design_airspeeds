import aircraft
from standard_atmosphere import *
from scipy.interpolate import interp1d

#
class Vb:
    def __init__(self):
        self.ac = aircraft.Aircraft()
        self.ug = np.empty(int(self.ac.ceiling_f00) + 1)
        self.kg = np.empty(int(self.ac.ceiling_f00) + 1)
        self.altitudes = np.empty(int(self.ac.ceiling_f00) + 1)
        self.vb = np.empty(int(self.ac.ceiling_f00) + 1, 4)
        self.ude = np.empty(int(self.ac.ceiling_f00) + 1)
        self.rough_air_speed = np.empty(int(self.ac.ceiling_f00) + 1)
        self.vc_gust_lf = np.empty(int(self.ac.ceiling_f00) + 1)

    def get_ude_vc(self, h):
        altitude = np.empty(3)
        ude = np.empty(3)

        if self.ac.ctype == 23:
            altitude[0] = 0
            altitude[1] = 6096
            altitude[2] = 15240
            altitude[3] = 50000
            ude[0] = 50.0          # Vb - fps
            ude[1] = 50.0          # Vb - fps
            ude[2] = 25.0          # Vb - fps
            ude[3] = 25.0          # Vb - fps
        else:
            altitude[0] = 0
            altitude[1] = 4573
            altitude[2] = 18288
            altitude[3] = 50000
            ude[0] = 56.0          # Vc - fps
            ude[1] = 44.0          # Vc - fps
            ude[2] = 20.86         # Vc - fps
            ude[3] = 20.86         # Vc - fps

        ude_func = interp1d(altitude, ude)
        return ude_func(h)

    def evaluate_ng(self, vs, w):
        pass


    def evaluate_rough_airspeed(self):
        pass