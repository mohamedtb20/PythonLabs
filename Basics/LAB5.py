d = {'nom': 'Dupuis', 'prenom': 'Jacque', 'age': 30}
#1
d['prenom']='Jacques'
print(d)
#2
#we use .keys to show the keys to go from dictionnary to list
print(list(d.keys()))
#3
#we use .values to show the values and list function to go from dictionnary to list
print(list(d.values()))
#4
print(list(d))
#5
#print the value of every thing and we add ther other strs
print(d['prenom'], d['nom'], 'a', d['age'], 'ans')