import aircraft
#
class Vb:
    def __init__(self):
        self.ac = aircraft.Aircraft()
        self.ug = np.empty(int(self.ac.ceiling_f00) + 1)
        self.kg = np.empty(int(self.ac.ceiling_f00) + 1)
        self.altitudes = np.empty(int(self.ac.ceiling_f00) + 1)
        self.vb = np.empty(int(self.ac.ceiling_f00) + 1, 4)   # VC given in Calibrated airspeed
        self.ude = np.empty(int(self.ac.ceiling_f00) + 1)

    def get_ude(self):
        altitudes = np.empty(4)
        udes = np.empty(4, 3)
        if self.ac.ctype == 23:
            altitude[0] = 0
            altitude[1] = 6096
            altitude[2] = 15240
            altitude[3] = 50000
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
            altitude[0] = 0
            altitude[1] = 4573
            altitude[2] = 18288
            altitude[3] = 50000
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
