f=open('hamm', 'r')
f2=open('ham2.txt','r')
s=f.read()
s2=f2.read()
k=s.split()
k2=s2.split()
L=[]
for x in k :
    for y in k2 :
        if x == y :
            L.append(x)
print(L)