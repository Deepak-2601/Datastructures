my_dict={"name":"deepak","gender":"male","address":"India","age":19}
def searching(dict,value):
    for key in dict:
        if dict[key]== value:
            return key,value
    return "Sorry Value does not exist"
print(searching(my_dict,"India"))