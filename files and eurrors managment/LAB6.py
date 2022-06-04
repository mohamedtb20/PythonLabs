from math import sin
try :
    i=float(input('entrer un nombre entre -3 et 3'))
    s=sin(i)/i
    if i==2 :
        raise ValueError #dayrin lte7t ayerreur mnghir y affichilek dik joumla w hadi dakhla f ay eurreur
    else :
        print(s)
except ZeroDivisionError:
    print('c est pas possible de diviser sur un nombre nul')
except :
    print('Vous qvew entrer une vqleur invalid')
else :
    print("good")
finally:
    print("bon courage")
