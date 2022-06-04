f=open("ham2.txt", 'r')
#on ouvre notre fichier avec read
s=f.read()
#on transforme avec p notre contenue en liste
p=s.split() #f hade l etat rahe 3edna ghi liste dik l9raya li 9rina l fichier mchat
#on relie notre fichier apres split
k=f.read()
#x str in notre liste
for x in p :
    #notre fichier devient chaque carractaire de la liste + un espace
    k = k + x + " "
print(k)