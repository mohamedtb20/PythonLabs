#average calculation
L=[14, 9, 6, 8, 12]
#we initialize the sum value
sum=0
for i in range(len(L)) :
    #we calculate the dum of the notes and we devise by the indexes
    sum = sum + L[i]
    i=i+1,
average = sum/i
print ("the average is average = %2.2f "%average)