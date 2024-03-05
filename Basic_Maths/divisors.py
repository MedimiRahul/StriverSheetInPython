# 1st method is to chceck all numbers upto half of it number to see 
import math
def divisor1(n):
    divisors=[1]
    for i in range(2,n//2+1):
        if n%i==0:
            divisors.append(i)
    print(divisors)

divisor1(40) 


# 2nd method is with each dision we are getting its another divisor also 

def divisor2(n):
    divisors=[1]
    for i in range(2,int(math.sqrt(n))):
        if n%i==0:
            divisors.append(i)
            divisors.append(n//i)
    if n%math.sqrt(n)==0:
        divisors.append(math.sqrt(n))
    print(divisors)            

divisor2(40)    
