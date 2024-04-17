#!/usr/local/bin/python3

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

#print(np.arange(0,11,1))

quality = ctrl.Antecedent( np.arange(0,11,1), 'Quality' )
quality.automf(number=3, names=['bad', 'good', 'delicious'])

service = ctrl.Antecedent( np.arange(0,11,1), 'Service' )
service.automf(number=3, names=['bad', 'acceptable', 'excellent'])

print(quality)
print(quality.universe)


tip = ctrl.Consequent(np.arange(0,21,1), 'Tip')
print(tip.universe)
print(quality.view())