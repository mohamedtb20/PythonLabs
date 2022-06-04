# we want to print the days of the week
# first we creat a list with the week days
L = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
#every day in L has an index starting from Monday : index 0
for i in range(len(L)) :
    print("the {} day of the week is {}".format(i+1,L[i]))
#we want to print only week-end days with while

while i>=4 and i<=6 :
    print(L[i])
    i=i+1