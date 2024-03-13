
# ^[[1,2,3],[4,5,6],[7,8,9]]
# ^[[7,4,1],[8,5,2],[9,6,3]]
# ^ rotation of matrix by 90 deg anticlockwise can be done 
# ^ using extraspace . so create a same matrix with all values none.
# ^ then each column in the original array would be row in reverse format.

# ^ in order to rotate array without using extra space what we can do is use transpose and then
# ^ each row thats all 

# ^ if clockwise then simple treanspose would rotate the array 90 deg clockwise 

def rotateanti1(mat):
    secondarymat=[[0]*(len(mat[0])) for i in range(len(mat))]
    for i in range(len(mat[0])):
        for j in range(len(mat)):
            secondarymat[i][len(secondarymat)-j-1]=mat[j][i]
    return secondarymat

print(rotateanti1([[1,2,3],[4,5,6],[7,8,9]]))        


# ^ lets do inplace 

def transpose(mat):
    for i in range(len(mat)):
        for j in range(i,len(mat[0])):
            mat[i][j],mat[j][i]=mat[j][i],mat[i][j]

def rotateanti2(mat):
    transpose(mat)
    for i in range(len(mat)):
        start=0
        end=len(mat[0])-1
        while start<=end:
            mat[i][start],mat[i][end]=mat[i][end],mat[i][start]
            start+=1
            end-=1

mat2=[[1,2,3],[4,5,6],[7,8,9]]
rotateanti2(mat2)
print(mat2)    
