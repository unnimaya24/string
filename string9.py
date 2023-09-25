marks=[90,81,78,93,100]

list=[]
i=0
while(i < len(marks)):
    if (marks[i] % 2 == 0):
        list.append(marks[i])
    i += 1
print(list)
