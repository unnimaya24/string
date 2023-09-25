test_stirng = input("String to search is : ")
total = 1
i = 0
while(i < len(test_stirng)):
   if(test_stirng[i] == ' ' or test_stirng == '\n' or test_stirng == '\t'):
      total = total + 1
   i +=1

print("Total Number of Words in our input string is :",total)