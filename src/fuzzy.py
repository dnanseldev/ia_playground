#!/usr/local/bin/python3.12

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

print(np.arange(0,11,1))

quality = ctrl.Antecedent( np.arange(0,11,1), 'Quality' )
service = ctrl.Antecedent( np.arange(0,11,1), 'Service' )

print("Hello Fuzzy")