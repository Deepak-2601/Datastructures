mlist=[1,2,3,4,5,6,7,8,9,10]
def unique_element(list):
    a=[]
    for i in list:
        if i in a:
            print(i)
            return False
        else:
            a.append(i)
    return True

print(unique_element(mlist))