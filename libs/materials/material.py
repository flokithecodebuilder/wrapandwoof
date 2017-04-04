import numpy as np
from numpy.linalg import inv

# This is the base class for all the materials
# You should use it whenever you want to do anything with any material
class Material:
    def __init__(self):
        return self

    def displaymatrixfactor(self):
        print self.matrix_factor

    def accountstrain(self, stress_x, stress_y, stress_xy):
        self.strain_matrix = np.dot(self.matrix_factor, np.matrix([[stress_x], [stress_y], [stress_xy]]))
        print self.strain_matrix

    def accountstress(self, strain_x, strain_y, strain_xy):
        self.stress_matrix = np.dot(inv(self.matrix_factor), np.matrix([[strain_x], [strain_y], [strain_xy]]))
        print self.stress_matrix
