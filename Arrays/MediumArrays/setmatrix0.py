
# ^ we have to make entire row and entire column of that element 0.
# ^ the basic method would be find all the zero locations 
# ^ and then for each and every location convert to zeros 
# ^ another method would be if zero encounter then replace its rows and cols with -1
# ^ atlast replace -1 with 0

def setmatrix0(A):
    locs=[]
    for i in range(len(A)):
        for j in  range(len(A[i])):
            if A[i][j]==0:
                locs.append([i,j])
    for i in range(len(locs)):
        x=locs[i][0]
        y=locs[i][1]
        for j in range(len(A[0])):
            A[x][j]=0
        for k in range(len(A)):
            A[k][y]=0

a=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]
setmatrix0(a)
print(a)                      


