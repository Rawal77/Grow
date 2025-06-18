import numpy as np

arr = np.random.randint(2,10,size=(3))
print("array1: ",arr)

arr2 = np.random.randint(2,10,size=(1,3))
print("\n array2: ",arr2)

print("\nBroadcasted : " ,np.add(arr,arr2))
