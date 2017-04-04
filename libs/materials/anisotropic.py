import numpy as np
from numpy.linalg import inv
from material import Material

class AnIsotropic(Material):
    def __init__(self, E_x, E_y, v_xy, G_xy):
        self.E_x = E_x
        self.E_y = E_y
        self.v_xy = v_xy
        self.G_xy = G_xy

        self.matrix_factor = np.matrix([
            [(float(1)/self.E_x), -1*(float(self.v_xy)/self.E_y), 0],
            [-1*(float(self.v_xy)/self.E_y), (float(1)/self.E_x), 0],
            [0, 0, float(1)/G_xy]
        ])



# Examples of using this class
# anis = AnIsotropic(10, 20, 2, 2)
# anis.displaymatrixfactor()
# anis.accountstrain(10, 15, 20);
# print anis.strain_matrix
