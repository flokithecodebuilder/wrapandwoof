import numpy as np
from numpy.linalg import inv
from material import Material

def egvisnone(none, not_none_one, not_none_two) :
    if (none == False & (not_none_one != False & not_none_two != False)):
        return True

class Isotropic(Material):
    def __init__(self, E = False, G = False, v = False):
        self.E = E
        self.G = G
        self.v = v

        if (egvisnone(self.E, self.G, self.v)):
            self.E = float(self.G) * (2 * (1 + self.v))
            print self.E
        elif (egvisnone(self.G, self.E, self.v)):
            self.G = float(self.E) / ( 2 * (1 + self.v))
            print self.G
        elif (egvisnone(self.v, self.G, self.E)):
            self.v = (float(self.E)/(2 * self.G)) - 1
            print self.v
        else:
            print 'Your isotropic material is over defined. Please define it more accurate'
        self.matrix_factor = np.matrix([
            [(float(1)/self.E), -1*(float(self.v)/self.E), 0],
            [-1*(float(self.v/self.E)), (float(1)/self.E), 0],
            [0, 0, (float(1)/self.G)]
        ]);

# Examples of using this class
# ias = Isotropic(E= 100, v= 10)
# ias.displaymatrixfactor()
# ias.accountstress(10,10,2)
# print ias.stress_matrix[2]
