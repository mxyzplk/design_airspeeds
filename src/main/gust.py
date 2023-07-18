import numpy as np
#
class Gust:
    def __init__(self):
        self.altitudes = np.empty(4)
        self.udes = np.empty(4, 3)
        self.define_ude()

    def define_ude(self):

        if self.ac.ctype == 23:
            self.altitude[0] = 0
            self.altitude[1] = 6096
            self.altitude[2] = 15240
            self.altitude[3] = 50000
            self.ude[0, 0] = 66.0          # Vb - fps
            self.ude[1, 0] = 66.0          # Vb - fps
            self.ude[2, 0] = 38.0          # Vb - fps
            self.ude[3, 0] = 38.0          # Vb - fps
            self.ude[0, 0] = 50.0          # Vc - fps
            self.ude[1, 0] = 50.0          # Vc - fps
            self.ude[2, 0] = 25.0          # Vc - fps
            self.ude[3, 0] = 25.0          # Vc - fps
            self.ude[0, 0] = 25.0          # Vd - fps
            self.ude[1, 0] = 25.0          # Vd - fps
            self.ude[2, 0] = 12.5          # Vd - fps
            self.ude[3, 0] = 12.5          # Vd - fps
        else:
            self.altitude[0] = 0
            self.altitude[1] = 4573
            self.altitude[2] = 18288
            self.altitude[3] = 50000
            self.ude[0, 0] = 56.0          # Vb - fps
            self.ude[1, 0] = 44.0          # Vb - fps
            self.ude[2, 0] = 20.86         # Vb - fps
            self.ude[3, 0] = 20.86         # Vb - fps
            self.ude[0, 0] = 56.0          # Vc - fps
            self.ude[1, 0] = 44.0          # Vc - fps
            self.ude[2, 0] = 20.86         # Vc - fps
            self.ude[3, 0] = 20.86         # Vc - fps
            self.ude[0, 0] = 56.0 * 0.5    # Vd - fps
            self.ude[1, 0] = 44.0 * 0.5    # Vd - fps
            self.ude[2, 0] = 20.86 * 0.5   # Vd - fps
            self.ude[3, 0] = 20.86 * 0.5   # Vd - fps

    def get_ude(self, h, vb, vc, vd, airspeed):
        pass