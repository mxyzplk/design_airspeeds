import numpy as np

class Atmosphere:
    def __init__(self, altitude, disa):
        self.h = altitude
        self.delta = 0
        self.theta = 0
        self.sigma = 0
        self.mu = 0
        self.cs = 0
        self.disa = disa
        self.rho = 0
        self.t = 0

        self.evaluate_atmosphere()

    def set_altitude(self, altitude, disa):
        self.h = altitude
        self.disa = disa
        self.evaluate_atmosphere()

    def evaluate_atmosphere(self):

        # Standard sea level pressure, temperature and air density:
        T0 = 288.15  # Standard temperature at sea level [K]
        p0 = 101325.0  # Standard pressure at sea level [Pa]
        rho0 = 1.225  # [kg/m3]
        gamma = 1.4

        # Standard acceleration due to gravity:
        g = 9.80665  # [kg*m/s2]

        # Specific gas constant for air:
        R = 287.058  # [J/(kg*K)]

        # Lapse rates and atmospheric zones self.hs:
        # TROPOSPHERE .......................................... (0-10.999)km
        h_ts = 0  # [m]
        a_ts = -0.0065  # [K/m]
        # TROPOPAUSE ========================================== (11-19.999)km
        h_tp = 11000  # [m]
        a_tp = 0  # [K/m] (isothermal)
        # STRATOSPHERE ........................................ (20-31.999)km
        h_ss1 = 20000  # [m]
        a_ss1 = 0.001  # [K/m]
        # ..................................................... (32-46.999)km
        h_ss2 = 32000  # [m]
        a_ss2 = 0.0028  # [K/m]
        # STRATOPAUSE ========================================= (47-50.999)km
        h_sp = 47000  # [m]
        a_sp = 0  # [K/m] (isothermal)
        # MESOSPHERE .......................................... (51-70.999)km
        h_ms1 = 51000  # [m]
        a_ms1 = -0.0028  # [K/m]
        # ......................................................... (71-85)km
        h_ms2 = 71000  # [m]
        a_ms2 = -0.002  # [K/m]
        # ===================================================================
        h_fin = 85000  # [m]

        # Temperature, pressure and density at the upper boundaries:
        # Upper boundary of troposphere: ....................................
        T_1 = T0 + a_ts * (h_tp - h_ts)
        p_1 = p0 * (T_1 / T0) ** (-g / (a_ts * R))
        rho_1 = rho0 * (T_1 / T0) ** (-g / (a_ts * R) - 1)
        # Upper boundary of tropopause: .....................................
        T_2 = T_1
        p_2 = p_1 * np.exp(-(g / (R * T_2)) * (h_ss1 - h_tp))
        rho_2 = rho_1 * np.exp(-(g / (R * T_2)) * (h_ss1 - h_tp))
        # Upper boundary of stratosphere (1): ...............................
        T_3 = T_2 + a_ss1 * (h_ss2 - h_ss1)
        p_3 = p_2 * (T_3 / T_2) ** (-g / (a_ss1 * R))
        rho_3 = rho_2 * (T_3 / T_2) ** (-g / (a_ss1 * R) - 1)
        # Upper boundary of stratosphere (2): ...............................
        T_4 = T_3 + a_ss2 * (h_sp - h_ss2)
        p_4 = p_3 * (T_4 / T_3) ** (-g / (a_ss2 * R))
        rho_4 = rho_3 * (T_4 / T_3) ** (-g / (a_ss2 * R) - 1)
        # Upper boundary of stratopause: ....................................
        T_5 = T_4
        p_5 = p_4 * np.exp(-(g / (R * T_5)) * (h_ms1 - h_sp))
        rho_5 = rho_4 * np.exp(-(g / (R * T_5)) * (h_ms1 - h_sp))
        # Upper boundary of mezosphere (1): .................................
        T_6 = T_5 + a_ms1 * (h_ms2 - h_ms1)
        p_6 = p_5 * (T_6 / T_5) ** (-g / (a_ms1 * R))
        rho_6 = rho_5 * (T_6 / T_5) ** (-g / (a_ms1 * R) - 1)
        # Upper boundary of mezosphere (2): .................................
        T_7 = T_6 + a_ms2 * (h_fin - h_ms2)

        # Temperature, pressure and density calculation:
        if self.h < h_tp:
            # In the troposphere:
            t_std = T0 + a_ts * (self.h - h_ts)
            p_std = p0 * (t_std / T0) ** (-g / (a_ts * R))
            rho_std = rho0 * (t_std / T0) ** (-g / (a_ts * R) - 1)

        elif self.h >= h_tp and self.h < h_ss1:
            # In the tropopause:
            t_std = T_1
            p_std = p_1 * np.exp(-(g / (R * t_std)) * (self.h - h_tp))
            rho_std = rho_1 * np.exp(-(g / (R * t_std)) * (self.h - h_tp))

        elif self.h >= h_ss1 and self.h < h_ss2:
            # In the stratosphere (1):
            t_std = T_2 + a_ss1 * (self.h - h_ss1)
            p_std = p_2 * (t_std / T_2) ** (-g / (a_ss1 * R))
            rho_std = rho_2 * (t_std / T_2) ** (-g / (a_ss1 * R) - 1)

        elif self.h >= h_ss2 and self.h < h_sp:
            # In the stratosphere (2):
            t_std = T_3 + a_ss2 * (self.h - h_ss2)
            p_std = p_3 * (t_std / T_3) ** (-g / (a_ss2 * R))
            rho_std = rho_3 * (t_std / T_3) ** (-g / (a_ss2 * R) - 1)

        elif self.h >= h_sp and self.h < h_ms1:
            # In the stratopause:
            t_std = T_4
            p_std = p_4 * np.exp(-(g / (R * t_std)) * (self.h - h_sp))
            rho_std = rho_4 * np.exp(-(g / (R * t_std)) * (self.h - h_sp))

        elif self.h >= h_ms1 and self.h < h_ms2:
            # In the mezosphere (1):
            t_std = T_5 + a_ms1 * (self.h - h_ms1)
            p_std = p_5 * (t_std / T_5) ** (-g / (a_ms1 * R))
            rho_std = rho_5 * (t_std / T_5) ** (-g / (a_ms1 * R) - 1)

        elif self.h >= h_ms2 and self.h <= h_fin:
            # In the mezosphere (2):
            t_std = T_6 + a_ms2 * (self.h - h_ms2)
            p_std = p_6 * (t_std / T_6) ** (-g / (a_ms2 * R))
            rho_std = rho_6 * (t_std / T_6) ** (-g / (a_ms2 * R) - 1)

        self.t = t_std + self.disa
        self.rho = rho_std / (1 + self.disa / t_std)
        self.delta = p_std / p0
        self.theta = self.t / T0
        self.sigma = self.rho / rho0
        self.cs = (gamma * R * self.t) ** 0.5

class Airspeed:
    def __init__(self, altitude, speed, vtype, disa):
        self.h = altitude
        self.speed = speed
        self.type = vtype
        self.cas = 0
        self.tas = 0
        self.eas = 0
        self.mach = 0
        self.disa = disa
        self.qdyn = 0

        self.atmos = Atmosphere(self.h, self.disa)

    def set_altitude(self, altitude, disa):
        self.h = altitude
        self.disa = disa
        self.atmos.set_altitude(self.h, self.disa)

    def evaluate_velocities(self):

        cso = 340.43  # Sound speed at sea level (m)
        T0 = 288.15  # Standard sea level temperature (K)
        p0 = 101325.0  # Standard pressure at sea level [Pa]
        gamma = 1.4
        g = 9.80665  # [kg*m/s2]

        if self.type == 'CAS':
            self.cas = self.speed
            self.eas = (2 * self.atmos.delta * cso ** 2 / (gamma - 1) * ((1 + 1 / self.atmos.delta * (
                        (1 + (gamma - 1) / 2 * (self.cas / cso) ** 2) ** (gamma / (gamma - 1)) - 1)) ** (
                                                                               (gamma - 1) / gamma) - 1)) ** 0.5
            self.mach = self.eas / (cso * (self.atmos.delta ** 0.5))
            self.tas = self.mach * self.atmos.cs


        elif self.type == 'Mach':
            self.mach = self.speed
            self.tas = self.mach * self.atmos.cs
            self.eas = cso * self.mach * self.atmos.delta ** 0.5
            self.cas = (2 * cso ** 2 / (gamma - 1) * ((1 + self.atmos.delta * (
                        (1 + (gamma - 1) / 2 * ((self.eas / cso) ** 2) / self.atmos.delta) ** (gamma / (gamma - 1)) - 1)) ** (
                                                                  (gamma - 1) / gamma) - 1)) ** 0.5


        elif self.type == 'EAS':
            self.eas = self.speed
            self.cas = (2 * cso ** 2 / (gamma - 1) * ((1 + self.atmos.delta * (
                        (1 + (gamma - 1) / 2 * ((self.eas / cso) ** 2) / self.atmos.delta) ** (gamma / (gamma - 1)) - 1)) ** (
                                                                  (gamma - 1) / gamma) - 1)) ** 0.5
            self.mach = self.eas / (cso * self.atmos.delta ** 0.5)
            self.tas = self.mach * self.atmos.cs


        elif self.type == 'TAS':
            self.tas = self.speed
            self.mach = self.tas / self.atmos.cs
            self.eas = cso * self.mach * self.atmos.delta ** 0.5
            self.cas = (2 * cso ** 2 / (gamma - 1) * ((1 + self.atmos.delta * (
                        (1 + (gamma - 1) / 2 * ((self.eas / cso) ** 2) / self.atmos.delta) ** (gamma / (gamma - 1)) - 1)) ** (
                                                                  (gamma - 1) / gamma) - 1)) ** 0.5

        self.qdyn = 0.5 * self.atmos.rho * self.eas ** 2
