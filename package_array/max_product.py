import numpy as np
myarray=np.array([10,20,30,40,50,60,70,80,90,100])
def find_max_product(array):
    maxproduct = 0
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if array[i] * array[j] > maxproduct:
                maxproduct = array[i] * array[j]
                pairs =str(array[i]) + "," + str(array[j])
    print(pairs)
    print(maxproduct)
find_max_product(myarray)