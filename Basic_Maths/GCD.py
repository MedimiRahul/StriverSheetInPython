# 1st method 

def GCD(a,b):
    tracked=None
    if a==b:
        return a
    if a<b:
        for i in range(1,a+1):
            if a%i==0 and b%i==0:
                tracked=i
        return tracked
    else:
        for i in range(1,b+1):
            if b%i==0 and a%i==0:
                tracked=i
        return tracked


# 2nd method using eucledean formula with the help of recursion 

def GCD2(a,b):
    if b==0:
        return a
    if a>b:
        return GCD2(b,a%b)  
    else:
        return GCD2(a,b%a) 
    
print(GCD2(9,11))    
        


