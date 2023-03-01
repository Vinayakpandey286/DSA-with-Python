# [11, 12, 13, 14]
# [21, 22, 23, 24]
# [31, 32, 33, 34]
# [41, 42, 43, 44]
def Searchin_Sorted_matrix(matrix,n,d):
    row=0
    col=n-1
    while(row<n and col>=0):
        if(matrix[row][col]==d):
            print(row)
            print(col)
            return
            
        elif(matrix[row][col]>d):
            col-=1
        else:
            row+=1
            
    print("Not Found")
        
if __name__ == '__main__':
    n=int(input())
    matrix=[]
    for i in range(n):
        arr=[]
        for j in range(n):
            arr.append(int(input()))
        
        matrix.append(arr)
        
    d=int(input())
    # for a in matrix:
    #     print(a)
    
    Searchin_Sorted_matrix(matrix,n,d)