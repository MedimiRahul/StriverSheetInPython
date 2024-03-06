# same as previous 

def freq(A):
    maxif=-9999999
    maxinum=None
    mininum=None
    minif=99999999
    counti={}
    for i in range(len(A)):
        counti.setdefault(A[i],0)
        counti[A[i]]+=1
    for i in counti:
        if counti[i]>maxif:
            maxif=counti[i]
            maxinum=i
        if counti[i]<minif:
            minif=counti[i]
            mininum=i
    return mininum,maxinum
print(freq([4,5,4,1,5]))            