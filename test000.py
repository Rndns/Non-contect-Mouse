import numpy as np
a = np.empty((0, 2))
a = np.append(a, [np.array((1, 2))])
a = np.append(a, [np.array((2, 3))])
print(a)