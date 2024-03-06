# 1st method is to use Array hashing . create the array with max number and then store its occurance 
def countfrequency(A):
    maxi=-9999999
    for i in range(len(A)):
        if A[i]>maxi:
            maxi=A[i]
    counti=[0 for i in range(maxi+1)]
    for i in range(len(A)):
        counti[A[i]]+=1
    return counti

print(countfrequency([2,4,2,7,1,0,0]))    


# second method is to use dictionary or map 

def countfrequency2(A):
    counti2={}
    for i in range(len(A)):
        counti2.setdefault(A[i],0)
        counti2[A[i]]+=1
    return counti2

print(countfrequency2([2,2,2,0,7,7,8]))    
    
