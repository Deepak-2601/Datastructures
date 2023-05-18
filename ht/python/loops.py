shopping = ["milk", "bread", "ice-cream", "spam", "butter", "rice", "eggs",  "cheese", "curd", "chocolates", "noodles"]
item = input("Enter the items please: ")
found = None
for i in range(len(shopping)): #TODO:find the range
    if shopping[i] == item:
        found = i
        break
if found is not None:
    print("The item that you are finding is at index {}".format(found))
else:
    print("Sorry  we couldn't find {} try again please".format(item))
