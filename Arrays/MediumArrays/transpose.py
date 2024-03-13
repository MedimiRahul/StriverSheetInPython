
# ^ transpose can be done in two ways 
# ^ using extra space storing each element in another array in its corresponding column row position
# ^ we can do in place 
# ^ a small logic would be for each row the matrix would becomes smaller 
# ^ suppose 3*3 then for first row 3*3 interchange for second row upto 2*2 and last row 1*1


def transpose1(mat):
    secondarymat=[[0]*len(mat[0]) for i in range(len(mat))]
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            secondarymat[j][i]=mat[i][j]
    return secondarymat


# ^ lets do inplace 

def transpose2(mat):
    for i in range(len(mat)):
        for j in range(i,len(mat[0])):
            mat[i][j],mat[j][i]=mat[j][i],mat[i][j]

mat=[[1,2,3],[4,5,6],[7,8,9]]
print(transpose1(mat))
transpose2(mat)
print(mat)            