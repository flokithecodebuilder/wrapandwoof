from math import cos,sin, pi, sqrt, atan;

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

    def dobuleAngleOffAxisToOnAxis(self, stress1, stress2, stress6):
        p = float(stress1 + stress2)/2;
        q = float(stress1 - stress2)/2;
        r = float(stress6);

        onaxis = {
            'x': p + q*cos(self.teta*2) + r*sin(self.teta*2),
            'y': p - q*cos(self.teta*2) - r*sin(self.teta*2),
            's': -q*sin(self.teta*2) + r*cos(self.teta*2)
        }
        return onaxis;

    def invariantOffAxisToOnAxis(self, stress1, stress2, stress6):
        I = float(stress1 + stress2)/2;
        R = sqrt(((float(stress1)-stress2)**2)*1/4+(stress6**2));
        q = float(stress1 - stress2)/2;
        r = float(stress6);
        teta0 = float(1)/2 * (atan(float(r)/q));

        onaxis = {
            'x': I + cos(2*(self.teta - teta0))*R ,
            'y': I - cos(2*(self.teta - teta0))*R,
            's': -sin(2*(self.teta - teta0))*R
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

    def calculateStrainOffAxisFromOnAxis(self, strain1, strain2, strain6):
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

class Transform():
    def __init__(self, teta, param1, param2, param3):
        return self;

    def transformDegreeToRadian(self, degree):
        return degree * 2 * pi / 360;

    def assignMN(self, teta):
        self.m = cos(teta);
        self.n = sin(teta);
