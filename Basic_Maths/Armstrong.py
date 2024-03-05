# 1st method is basic iterate each num

def arm1(n):
    x=str(n)
    l=len(x)
    sumi=0
    for i in x:
        sumi+=(int(i)**l)
    if sumi==n:
        return True 
    return False

print(arm1(170))    