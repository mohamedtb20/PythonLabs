L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#1
#by adding 1 to every element the 0 will not be in the list and the 9 become 10
L.remove(0)
L.append(10)
print(L)
#2
#we will use insert function to add an element to the last place in L
L.insert(10,11)
print(L)
#3
#we will use insert but you should remove the last insert to get the result
L.insert(10,11)
L.insert(11,12)
print(L)
#4
#we print the first element
print(L[0])
#we print the first two elements
print(L[0:2],L[0:2], L[12], L[11:13])
#5
L.insert(3,3.5)
print(L)
#6
L.remove(3.5)
print(L)
#7
L.reverse()
print(L)
# 8
# we must run all the L elements to see if the Number that the user enter is available so we loop all L indexes and
# we test element by element
N=int(input("please enter a number"))
n=len(L)
for i in range(n) :
    if L[i] == N :
        print("exist")
    else :
        print("don't exist")


