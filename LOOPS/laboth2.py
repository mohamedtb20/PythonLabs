limiteInf = int(input("Saisir la limite inférieur : "))
limiteSup = int(input("Saisir la limite supérieur : "))

print("Nombres premiers entre", limiteInf, " et ", limiteSup, " sont :")

for num in range(limiteInf, limiteSup + 1):
   # tous les nombres premiers sont supérieurs à 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
                print(num)

