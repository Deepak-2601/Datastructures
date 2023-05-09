def permutations_char(l1,l2):
    if len(l1)!= len(l2):
        return  False
    l1.sort()
    l2.sort()
    if l1 == l2:
        return "Is permutable"
    else:
        return "Not permutable"

list1=['a','b','c']
list2=['c','b','a']
print(permutations_char(list1,list2))