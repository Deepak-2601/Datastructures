new_tuples=('h','e','l','l','o')
#print('e'in  new_tuples)
#print(new_tuples.index('p'))

def searching (n_tuple,value):
    for i in range(len(n_tuple)):
        if n_tuple[i] == value:
            return f"Element found at position {i}"
    return "Sorry element not found"

print(searching(new_tuples,'h'))