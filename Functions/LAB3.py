#the factorial function will multiply all numbers under the number that you enter
def factorial(n) :
    #we will loop from 1 to your number
    x=1
    for i in range(1,n+1):
        x=x*i
    return x
n=int(input('give a number: '))
print ('the factorial of {} is {}'.format(n,factorial(n)))



