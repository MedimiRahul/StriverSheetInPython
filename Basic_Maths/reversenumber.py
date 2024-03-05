# 1st method /
# using two pointer 


def reverse1(n):
    a=str(n)
    x=[i for i in a]
    for i in range(len(x)//2):
        x[i],x[len(x)-i-1]=x[len(x)-i-1],x[i]
    return ''.join(x)

print(reverse1(1234))    
