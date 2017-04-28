from math import pow

class StressStrainRelation():
    def __init__(self, E = None, S = None, Q = None):

        if( E != None and S == None and Q == None):
            self.assignE(E);
            self.calculateSFromE();
            self.calculateQFromE();
        elif( E == None and S != None and Q == None):
            self.assignS(S);
            self.calculateEFromS();
            self.calculateQFromE();
        elif( E == None and S == None and Q != None):
            self.assignQ(Q);
            self.calculateEFromQ();
            self.calculateSFromE();
        else:
            print 'some thing is not right :(';

    def assignE(self, E):
        self.ex = E[0];
        self.ey = E[1];
        self.es = E[2];
        self.vx = E[3];
        self.vy = E[4];

    def assignS(self, S):
        self.sxx = S[0];
        self.syy = S[1];
        self.sss = S[2];
        self.sxy = S[3];
        self.syx = S[4];

    def assignQ(self, Q):
        self.qxx = Q[0];
        self.qyy = Q[1];
        self.qss = Q[2];
        self.qxy = Q[3];
        self.qyx = Q[4];

    def calculateEFromS(self):
        self.ex = 1.0/self.sxx;
        self.ey = 1.0/self.syy;
        self.es = 1.0/self.sss;
        self.vx = (-1.0)*self.syx/self.sxx;
        self.vy = (-1.0)*self.sxy/self.syy;

    def calculateSFromE(self):
        self.sxx = (1.0/self.ex);
        self.sxy = (float(self.vy)/self.ey);
        self.syy = (1.0/self.ey);
        self.syx = (float(self.vx)/self.ex);
        self.sss = (1.0/self.es);

    def calculateEFromQ(self):
        m = (1- (float(self.qxy)/self.qxx)*(float(self.qyx)/self.qyy)) ** -1;
        self.ex = float(self.qxx)/m;
        self.ey = float(self.qyy)/m;
        self.es = float(self.qss);
        self.vx = float(self.qyx)/self.qyy;
        self.vy = float(self.qxy)/self.qxx;


    def calculateQFromE(self):
        m = (1- self.vx*self.vy) ** -1;
        self.qxx = m*self.ex;
        self.qxy = m*self.vy*self.ex;
        self.qyy = m*self.ey;
        self.qyx = m*self.vx*self.ey;
        self.qss = self.es;

    def calculateStrain(self, stressx, stressy, stresss):
        strain = {
            'x': self.sxx*stressx + self.sxy*stressy,
            'y': self.syy*stressy + self.syx*stressx,
            's': self.sss*stresss
        }
        return strain;

    def calculateStress(self, strainx, strainy, strains):
        stress = {
            'x': self.qxx*strainx + self.qxy*strainy,
            'y': self.qyy*strainy + self.qyx*strainx,
            's': self.qss*starins
        }
        return strain;
