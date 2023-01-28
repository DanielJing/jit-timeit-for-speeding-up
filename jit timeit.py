# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 15:57:09 2023

@author: Administrator
"""

import timeit
import numpy as np
from numba import jit

n = 10**10

def func(s, n):
    for i in range (1,n):
        s = s+1/i
    return s

start = timeit.timeit()
print("Euler's constant is: {:9.8f}".format(func(0,1) - np.log(n)))

end = timeit.timeit()
print("Elapsed time is: {:9.8f} seconds".format(end - start))