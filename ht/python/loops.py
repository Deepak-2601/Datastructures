shopping = ["milk", "bread", "ice-cream", "spam", "butter", "rice", "cheese", "curd", "chocolates", "noodles"]
item = "curd"
found = None
for i in range(len(shopping)):
    if shopping[i] == item:
        found = i
        break
if found is not None:
    print("The item that you are finding is at index {}".format(found))
else:
    print("Sorry {} is not found".format(item))
