# 1st method 

def palin1(n):
    x=str(n)
    for i in range(len(x)//2):
        if x[i]!=x[len(x)-1-i]:
            return False
    return True

   