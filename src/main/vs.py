import numpy as np


class Vs:
    def __init__(self, aircraft_ceiling_f00, aircraft_ceiling_fxx, weights, clmax_f00, clmax_fxx):

        self.altitude_f00 = np.empty(int(aircraft_ceiling_f00))
        self.altitude_fxx = np.empty(int(aircraft_ceiling_fxx))

        self.vs_f00 = np.empty((int(aircraft_ceiling_f00), len(weights)))
        self.vs_fxx = np.empty((int(aircraft_ceiling_fxx), len(weights)))

        Vs.get_vs_f00(clmax_f00, weights)
        Vs.get_vs_f00(clmax_fxx, weights)

    def get_vs_f00(self, clmax, weights):
        pass

    def get_vs_fxx(self, clmax, weights):
        pass