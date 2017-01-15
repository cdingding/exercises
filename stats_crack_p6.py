# Crack stats, random chooose 6 out of continuous values, probability of population mean in the range of the six?
import numpy as np
m = 0
n = 0
lst = np.random.sample(1000)
theMean = lst.mean()
for i in range(100000):
    choice = np.random.choice(lst,6)
    if theMean < max(choice) and theMean > min(choice):
        m += 1
    n += 1
print float(m)/n
