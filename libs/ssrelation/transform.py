from math import cos,sin, pi

class TransformSS():
    def __init__(self, teta):
        self.teta = self.transformDegreeToRadian(teta);
        self.assignMN(self.teta);

    def transformDegreeToRadian(self, degree):
        return degree * 2 * pi / 360;

    def assignMN(self, teta):
        self.m = cos(teta);
        self.n = sin(teta);

    def calculateStressOnAxisFromOffAxis(self, stress1, stress2, stress6):
        onaxis = {
            'x': float(self.m**2)*stress1 + (self.n**2)*stress2 + 2*self.m*self.n*stress6,
            'y': float(self.n**2)*stress1 + (self.m**2)*stress2 - 2*self.m*self.n*stress6,
            's': float(-1*self.m*self.n)*stress1 + (self.m*self.n*stress2) + ((self.m**2)-(self.n**2))*stress6
        }
        return onaxis;

    def calculateStressOffAxisFromOnAxis(self, stress1, stress2, stress6):
        self.teta = -self.teta;
        self.assignMN(self.teta);
        offaxis = {
            '1': float(self.m**2)*stress1 + (self.n**2)*stress2 + 2*self.m*self.n*stress6,
            '2': float(self.n**2)*stress1 + (self.m**2)*stress2 - 2*self.m*self.n*stress6,
            '6': float(-1*self.m*self.n)*stress1 + (self.m*self.n*stress2) + ((self.m**2)-(self.n**2))*stress6
        }
        self.teta = -self.teta;
        self.assignMN(self.teta);
        return offaxis;

    def calculateStrainOnAxisFromOffAxis(self, strain1, strain2, strain6):
        onaxis = {
            'x': float(self.m**2)*strain1 + (self.n**2)*strain2 + self.m*self.n*strain6,
            'y': float(self.n**2)*strain1 + (self.m**2)*strain2 - self.m*self.n*strain6,
            's': float(-1*self.m*self.n)*strain1*2 + (self.m*self.n*strain2)*2 + ((self.m**2)-(self.n**2))*strain6
        }
        return onaxis;

    def calculateStressOffAxisFromOnAxis(self, strain1, strain2, strain6):
        self.teta = -self.teta;
        self.assignMN(self.teta);
        offaxis = {
            '1': float(self.m**2)*strain1 + (self.n**2)*strain2 + self.m*self.n*strain6,
            '2': float(self.n**2)*strain1 + (self.m**2)*strain2 - self.m*self.n*strain6,
            '6': float(-1*self.m*self.n)*strain1*2 + (self.m*self.n*strain2)*2 + ((self.m**2)-(self.n**2))*strain6
        }
        self.teta = -self.teta;
        self.assignMN(self.teta);
        return offaxis;
