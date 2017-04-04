class FiberVolumeFraction:
    def __init__(self, volume_fibers, volume_matrix):
        self.volume_fibers = volume_fibers
        self.volume_matrix = volume_matrix
        self.total_volume = volume_fibers + volume_matrix

        self.volume_fraction = self.accountvolumefraction()
        self.matrix_volume_fraction = self.accountmatrixvolumefraction()

    def accountvolumefraction(self):
        return (float(self.volume_fibers)/self.total_volume)

    def accountmatrixvolumefraction(self):
        return (float(self.volume_matrix)/self.total_volume)

    def accountmassfractionfromvolume(self, sp_mass_fiber, sp_mass_matrix):
        return (float(self.volume_fraction) * sp_mass_fiber) / ((float(self.volume_fraction) * sp_mass_fiber) + (float(self.matrix_volume_fraction) * sp_mass_matrix))

    def accountdensityfromvolume(self, sp_mass_fiber, sp_mass_matrix):
        return (float(self.volume_fraction)*sp_mass_fiber + float(self.matrix_volume_fraction)*sp_mass_matrix)

# Examples of using this class
#temp = FiberVolumeFraction(10, 5)
#print temp.matrix_volume_fraction
