def equal_pairs(number,target):
    for i in range(len(number)):
        for j in range(i+1,len(number)):
            if number[i] == number[j]:
                continue
            elif number[i] + number[j] == target:
                print(i,j)

                
l1=[1,2,4,6,9,17]
equal_pairs(l1,7)