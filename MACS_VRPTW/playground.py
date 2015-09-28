__author__ = 'Lada'

import time
import numpy as np


start = time.time()
print "hello"


data=np.loadtxt('solomon_r101.txt', skiprows=1)
end = time.time()
print end - start