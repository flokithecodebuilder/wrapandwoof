class FiberMassFraction:
    def __init__(self, mass_fibers, mass_matrix):
        self.mass_fibers = mass_fibers
        self.mass_matrix = mass_matrix
        self.total_mass = mass_fibers + mass_matrix

        self.mass_fraction = self.accountmassfraction()
        self.matrix_mass_fraction = self.accountmatrixmassfraction()

    def accountmassfraction(self):
        return (float(self.mass_fibers)/self.total_mass)

    def accountmatrixmassfraction(self):
        return (float(self.mass_matrix)/self.total_mass)

    def accountvolumefractionfrommass(self, sp_mass_fiber, sp_mass_matrix):
        return (float(self.mass_fraction)/sp_mass_fiber) / ((float(self.mass_fraction)/sp_mass_fiber) + (float(self.matrix_mass_fraction)/sp_mass_matrix))

    def accountdensityfrommass(self, total_volume):
        return (float(self.mass_fibers)/total_volume + float(self.mass_matrix)/total_volume)

# Examples of using this class
# temp = FiberMassFraction(10, 5)
# print temp.matrix_mass_fraction
