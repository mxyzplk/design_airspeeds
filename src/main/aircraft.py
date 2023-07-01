import os
import numpy as np


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

        # aerodynamic data
        self.dclda = None
        self.clmax_f00 = None
        self.clmax_fxx = None
        self.vc = []
        self.resources_dir = None
        self.results_dir = None

        self.get_dirs()
        self.read_mass()
        self.read_vc()
        self.read_clmax_f00()
        self.read_clmax_fxx()

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
            pass
        
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
