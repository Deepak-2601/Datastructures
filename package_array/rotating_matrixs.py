import numpy as np
a1=np.array([ [10,20,30], [40,50,60], [70,80,90] ])
def rotate(matrix):
    l= len(matrix)
    for layer in range(l//2):
        first=layer
        last=l-layer-1
        for i in range(first,last):
            top = matrix[layer][i]
            matrix[layer][i]=matrix[-i-1][layer]
            matrix[-i-1][layer]=matrix[-layer-1][-i-1]
            matrix[-layer - 1][-i - 1]=matrix[i][-layer-1]
            matrix[i][-layer-1]=top
    return matrix
print(a1)
print(rotate(a1))