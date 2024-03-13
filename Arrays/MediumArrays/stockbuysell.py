
# ^ so buying a lower cost and selling at higher cost is the motto 
# ^ so brute force approcah will be check each and every pair and find the differnce 

# ^ but it would be o(n^2)

# ^ so beautifully the optimized the code 
# ^ so the linearly transversed and in that transversal they are comparing minimum and maxsofar like 
# ^ that concept 

def stockbuysell(A):
    mini=999999999
    maxsofar=0
    for i in range(len(A)):
        if A[i]<mini:
            mini=A[i]
        maxi=A[i]-mini  
        if maxi>maxsofar:
            maxsofar=maxi
    return maxsofar

print(stockbuysell([7,6,4,3,1]))     