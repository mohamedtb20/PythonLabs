import os
list = os.listdir('C:\\Windows')
print(list)
try :
    list2 = os.listdir("C:\\Users\\DELL\\OneDrive\\Bureau")
    print(list2)
except  FileNotFoundError :
    print('the path is incorrect')
else :
    print('good bye !')
finally:
    print('l3ez w nser')
