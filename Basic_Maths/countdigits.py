# 1st method 

def countdigits1(n):
    a=str(n)
    return len(a)

# 2nd method 

def countdigits2(n):
    count=0
    x=1
    while True:
        if n/x>1:
            count+=1
            x*=10
        else:
            return count

     
