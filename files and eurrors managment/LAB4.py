f=open("ham2.txt", 'r')
s=f.read()
k=s.split()

motmax=""
for x in k :
        if x > motmax :
            motmax=x
print("{} est le plus long ".format(motmax))

