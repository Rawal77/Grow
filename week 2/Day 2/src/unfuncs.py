import numpy as np

arr1 = np.array([[1,2,3],[2,4,5]])
arr2 = np.array([2,4,5])

add = np.add(arr1,arr2)

# Add 
print(add)

# Sum
print(np.sum(add))

# Mean
print(np.mean(add))

# Standard Deviation
print(np.std(add))

# Argmin & Argmax

#               For 1-dim
arr = np.array([5,6,1,2,3])
print('For 1 dim smallest value of index is ',np.argmin(arr))
print('For 1 dim largest  value of index is',np.argmax(arr))


#               For 2-dim
# add ---> [[ 3  6  8]
#          [ 4  8 10]]
print('\nFor 2 dim smallest value of index is ',np.argmin(add))
print('For 2 dim largest  value of index is',np.argmax(add))





