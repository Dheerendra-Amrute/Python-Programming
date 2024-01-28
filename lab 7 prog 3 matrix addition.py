#3. Write a method to compute addition of two matrices to get a resultant matrix. 
#Call this method in main to have A= B+C+D(where A,B,C,D are matrices).

def sum_matrix(B,C,D):
    A=[[0,0,0],[0,0,0],[0,0,0]]
    for i in range(len(B)):
        for j in range(len(B[i])):
            A[i][j]=B[i][j]+C[i][j]+D[i][j]
    return A
B=[[1,2,3],[4,5,6],[7,8,9]]
C=[[3,2,1],[6,5,4],[9,8,7]]
D=[[9,8,7],[6,5,4],[3,2,1]]
resultant = sum_matrix(B,C,D)
print('resultant matrix :')
for i in resultant:
    print(i)

