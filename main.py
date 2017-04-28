from libs.materials.material import Material;
from libs.materials.isotropic import Isotropic;
from libs.materials.anisotropic import AnIsotropic;
from libs.characteristics.fibermassfraction import FiberMassFraction;
from libs.characteristics.fibervolumefraction import FiberVolumeFraction;
from libs.ssrelation.mainssrelation import StressStrainRelation;
from libs.ssrelation.transform import TransformSS;
from math import cos,sin, pi

############## Chapter 1 #################

## Example 1 - Chap 1 Tsai -- uncomment for run
#s = [5.525, 97.09, 139.5, -1.547, -1.547];
#temp = StressStrainRelation(S = s);
#print temp.calculateStrain(400, 60, 15);

## Example 2 - Chap 1 Tsai -- uncomment for run
#s = [25.91, 120.9, 241.5, -6.744, -6.744];
#temp = StressStrainRelation(S = s);
#print temp.calculateStrain(400, 60, 15);

## Example 3 - Chap 1 Tsai -- uncomment for run
#q = [181.8, 10.34, 7.17, 2.897, 2.897];
#temp = StressStrainRelation(Q = q);
#print temp.calculateStress(2.117, 5.206, 2.092);

## Example 4 - Chap 1 Tsai -- uncomment for run
#q = [39.16, 8.392, 4.14, 2.182, 2.182];
#temp = StressStrainRelation(Q = q);
#print temp.calculateStress(9.959, 4.556, 3.632);

############## Chapter 2 #################

## Example 1 - Chap 2 Tsai -- uncomment for run
#temp = TransformSS(45);
#print temp.calculateStressOnAxisFromOffAxis(9,3,4);

## Example 2 - Chap 2 Tsai -- uncomment for run
temp = TransformSS(45);
print temp.calculateStressOffAxisFromOnAxis(8,4,-6);
