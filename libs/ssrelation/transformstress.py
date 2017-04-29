import Transform from transform;
from math import cos,sin, pi, sqrt, atan;

class StressTransform(Transform):
    __init__(self, teta, stress1, stress2, stress6):
        self.teta = self.transformDegreeToRadian(teta);
        self.assignMN(self.teta);
        self.stress1 = stress1;
        self.stress2 = stress2;
        self.stress6 = stress6;
        self.p = (float(self.stress1)+self.stress2)/2;
        self.q = (float(self.stress1)-self.stress2)/2;
        self.r = (float(self.stress6));
        self.I = (float(self.stress1)+self.stress2)/2;
        self.R = sqrt(((float(self.stress1)-self.stress2)**2)*1/4+(self.stress6**2));
        self.teta0 = (atan(float(r)/q))/2;
