import os
import numpy as np
from common_functions import kg2lb, sqm2sqft


class Aircraft:
    def __init__(self):
        # design weights
        self.mtow = 0
        self.mzfw = 0
        self.mlw = 0
        self.mow = 0
        self.weights = []
        self.weight_label = []

        # aircraft data
        self.ctype = 0
        self.ceiling_f00 = 0
        self.ceiling_fxx = 0
        self.s = 0
        self.b = 0
        self.mac = 0
        self.name = None
        self.disa = 0
        self.atype = None

        # aerodynamic data
        self.dclda = None
        self.clmax_f00 = None
        self.clmax_fxx = None

        # vc data
        self.vc = []
        self.vc_limitation = []

        # directories
        self.resources_dir = None
        self.results_dir = None

        self.get_dirs()
        self.read_mass()
        self.read_vc()
        self.read_clmax_f00()
        self.read_clmax_fxx()

        self.ws = kg2lb(self.mtow) / sqm2sqft(self.s)

    def get_dirs(self):

        current_dir = os.path.dirname(os.path.abspath(__file__))

        self.resources_dir = os.path.join(current_dir, 'src', 'resources')
        self.results_dir = os.path.join(current_dir, 'src', 'results')

        if os.path.exists(self.results_dir):
            pass
        else:
            os.makedirs(self.results_dir)

    def read_ac_data(self):

        file_path = os.path.join(self.resources_dir, 'ac_data.txt')

        with open(file_path, 'r') as file:
            temp = file.readline().split()
            self.s = float(temp[0])
            temp = file.readline().split()
            self.b = float(temp[0])
            temp = file.readline().split()
            self.mac = float(temp[0])
            temp = file.readline().split()
            self.ceiling_fxx = float(temp[0])
            temp = file.readline().split()
            self.ceiling_f00 = float(temp[0])
            temp = file.readline().split()
            self.disa = float(temp[0])
            temp = file.readline().split()
            self.ctype = int(temp[0])
            if ctype == 23:
                temp = file.readline().split()
                self.atype = temp[0]

    def read_mass(self):

        file_path = os.path.join(self.resources_dir, 'mass.txt')

        with open(file_path, 'r') as file:
            temp = file.readline().split()
            self.mtow = float(temp[0])
            self.weights.append(float(temp[0]))
            self.weight_label.append(float(temp[1]))
            temp = file.readline().split()
            self.mlw = float(temp[0])
            self.weights.append(float(temp[0]))
            self.weight_label.append(float(temp[1]))
            temp = file.readline().split()
            self.mzfw = float(temp[0])
            self.weights.append(float(temp[0]))
            self.weight_label.append(float(temp[1]))
            temp = file.readline().split()
            self.mow = float(temp[0])
            self.weights.append(float(temp[0]))
            self.weight_label.append(float(temp[1]))

    def read_dclda(self):

        file_path = os.path.join(self.resources_dir, 'dclda.txt')
        with open(file_path, 'r') as file:
            temp = file.readline().split()
            nps = int(temp[0])
            self.dclda = np.empty((nps, 2))
            for i in range(nps):
                temp = file.readline().split()
                self.dclda[i, 0:1] = temp[0:1]

    def read_vc(self):

        file_path = os.path.join(self.resources_dir, 'vc.txt')
        with open(file_path, 'r') as file:
            temp = file.readline().split()
            self.vc.append(float(temp[0]) * 0.514444444)    # CAS limitation
            temp = file.readline().split()
            self.vc.append(float(temp[0]))                  # Mach limitation
            temp = file.readline().split()
            self.vc_limitation.append(int(temp[0]))
            if self.vc_limitation[0] == 1:                  # Low Altitude limitation
                self.vc_limitation.append(float(temp[1]))
                self.vc_limitation.append(float(temp[2]))


    def read_clmax_f00(self):

        file_path = os.path.join(self.resources_dir, 'clmax_f00.txt')

        with open(file_path, 'r') as file:
            temp = file.readline().split()
            nps = int(temp[0])
            self.clmax_f00 = np.empty((nps, 2))
            for i in range(nps):
                temp = file.readline().split()
                self.clmax_f00[i, 0:1] = temp[0:1]

    def read_clmax_fxx(self):

        file_path = os.path.join(self.resources_dir, 'clmax_fxx.txt')

        with open(file_path, 'r') as file:
            temp = file.readline().split()
            nps = int(temp[0])
            self.clmax_fxx = np.empty((nps, 2))
            for i in range(nps):
                temp = file.readline().split()
                self.clmax_fxx[i, 0:1] = temp[0:1]
