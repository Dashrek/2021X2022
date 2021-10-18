import numpy as np
a=np.array([[1,2,3,4],[2,3,4,5],[3,4,5,6],[6,7,8,9]])
#print(a[:])
print(np.array(list(a[:,:2].T)+[list(np.mean(a[:,2:],axis=1))]).T)
print("darekrs".find("rs"))