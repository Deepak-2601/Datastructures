import numpy as np
l2= np.array([10,20,30,40,50,60,70,80,90,100])
def finding_number(array,no):
    for i in range(len(array)):
        if array[i] == no:
            print(i)

finding_number(l2,50)