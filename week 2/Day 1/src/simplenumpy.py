# Convert a Python list [1,2,3,4] into a NumPy array; print its shape and dtype

import numpy as np

arr = [1,2,3,4]

print(type(arr))

narr = np.array(arr)
print(narr.dtype)
print(np.shape(narr))