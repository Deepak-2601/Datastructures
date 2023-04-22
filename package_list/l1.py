mylist=list()
while True:
    inp=input("Enter a number")
    if inp=="Done":
        break
    value=float(inp)
    mylist.append(value)
avg=sum(mylist)/len(mylist)

print("Average:",avg)