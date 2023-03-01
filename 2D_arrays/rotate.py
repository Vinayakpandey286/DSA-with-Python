def transpose(n,matrix):
    val=0
    for i in range(n):
        for j in range(val,n):
            temp=matrix[j][i]
            matrix[j][i]=matrix[i][j]
            matrix[i][j]=temp
            
        val+=1
    # print("transpose")
    # for val in matrix:
    #     print(val)
        
    col_swap(n,matrix)
    
def col_swap(n,matrix):
    lcol,rcol=0,n-1
    while (lcol<=rcol):
        for i in range(n):
            temp=matrix[i][rcol]
            matrix[i][rcol]=matrix[i][lcol]
            matrix[i][lcol]=temp
        lcol+=1
        rcol-=1
    
    # print("swap")
    for i in range(n):
        for j in range(n):
            print(matrix[i][j],end=" ")
        print()
            
        
        
        
if __name__ == '__main__':
    n=int(input())
    matrix=[]
    
    for i in range(n):
        arr=[]
        for j in range(n):
            arr.append(int(input()))
        
        matrix.append(arr)

    transpose(n,matrix)