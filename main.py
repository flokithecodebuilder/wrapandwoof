from libs.materials.material import Material
from libs.materials.isotropic import Isotropic
from libs.materials.anisotropic import AnIsotropic
from libs.characteristics.fibermassfraction import FiberMassFraction
from libs.characteristics.fibervolumefraction import FiberVolumeFraction
from libs.ssrelation.mainssrelation import StressStrainRelation

## Example 1 Tsai -- uncomment for run
#s = [5.525, 97.09, 139.5, -1.547, -1.547];
#temp = StressStrainRelation(S = s);
#print temp.calculateStrain(400, 60, 15);

## Example 2 Tsai -- uncomment for run
#s = [25.91, 120.9, 241.5, -6.744, -6.744];
#temp = StressStrainRelation(S = s);
#print temp.calculateStrain(400, 60, 15);

## Example 3 Tsai -- uncomment for run
q = [181.8, 10.34, 7.17, 2.897, 2.897];
temp = StressStrainRelation(Q = q);
print temp.calculateStress(2.117, 5.206, 2.092);
