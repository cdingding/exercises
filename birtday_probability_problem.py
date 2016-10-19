
import numpy as np

bdays = 365 - np.arange(23)
bdays_p = bdays/365.0

print 1- reduce(lambda x, y: x * y, bdays_p)

