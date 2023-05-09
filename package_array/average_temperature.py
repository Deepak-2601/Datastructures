num_days = input("Enter how many day's temperature ")
t = 0
temp=[]

for i in range(num_days):
    next = int(input("Days" + str(i+1) +"'s high temperature:"))
    temp.append(next)
    t +=temp[i]

average=round(t/num_days,2)
print("Average=",+ str(average))
above=0
for i in temp:
    if i > average:
        above +=1
print(str(above)+"days above average")

