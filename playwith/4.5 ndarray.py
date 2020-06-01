import time
import numpy as np
import math

aAarray = np.arange(1,100,0.1)
t_n1 = time.process_time()
b = math.pow(aAarray,2)
t_n2 = time.process_time()

bAarray = np.arange(1,100,0.1)
t_m1 = time.process_time()
c = np.power(bAarray,2)
t_m2 = time.process_time()

print(t_n2-t_n1)
print(t_m1-t_m1)