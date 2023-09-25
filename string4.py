
s = str(input("enter the string"))
reversedString=[]
index = len(s) 
while index > 0: 
    reversedString += s[ index - 1 ] 
    index = index - 1 
print(reversedString) 
