import os
import numpy as np


class Aircraft:
    def __init__(self):
        # design weights
        self.mtow = 0
        self.mzfw = 0
        self.mlw = 0
        self.mow = 0

        # aircraft data
        self.ctype = 0
        self.ceiling_f00 = 0
        self.ceiling_fxx = 0
        self.s = 0
        self.b = 0
        self.mac = 0

        # aerodynamic data
        self.dclda = None
        self.clmax_f00 = None
        self.clmax_fxx = None
        self.vc = None
        self.resources_dir = None

    def get_resources_dir(self):

        current_dir = os.path.dirname(os.path.abspath(__file__))

        self.resources_dir = os.path.join(current_dir, 'src', 'resources')

    def read_mass(self):

        file_path = os.path.join(self.resources_dir, 'mass.txt')

        with open(file_path, 'r') as file:
            temp = file.readline().split()
            self.mtow = temp[0]
            temp = file.readline().split()
            self.mlw = temp[0]
            temp = file.readline().split()
            self.mzfw = temp[0]
            temp = file.readline().split()
            self.mow = temp[0]

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
            nps = int(temp[0])
            self.vc = np.empty((nps, 2))
            for i in range(nps):
                temp = file.readline().split()
                self.vc[i, 0:1] = temp[0:1]

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
