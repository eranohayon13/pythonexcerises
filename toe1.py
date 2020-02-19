l=[]
# creating an empty list to store the results.
for i in range(2000, 3201):
# for loop iterating between the range 2000 and 3200, that also includes 2000 and 3200 (included 3201).
  if (i%7==0) and (i%5!=0):
    l.append(str(i))
# if the numbers within the given range are divisible 7 and is not a multiple of 5 then add the iterated number  to the previously created empty list l as a string.
print (','.join(l))
# print the sequence of the list but add a comma after every iterable element that was added to the string.