# [21, 22, 28, 31, 32]
# [41, 42, 55, 2, 77]
# [33, 99, 54, 11, 101]
# [42, 43, 46, 49, 21]
# [134, 167, 214, 324, 456]
def Saddle_price(matrix,n):  
    for i in range(n):
        min_row=0
        for j in range(1,n):
            if (matrix[i][j]<matrix[i][min_row]):
                min_row=j
                
                
        potential_ans=True
        for r in range(n):
            # print(col)
            if (matrix[i][min_row]<matrix[r][min_row]):
                potential_ans=False
                break
        if(potential_ans==True):
            print(matrix[i][min_row])
            return
    print("Invalid input")
    
        
if __name__ == '__main__':
    n=int(input())
    matrix=[]
    for i in range(n):
        arr=[]
        for j in range(n):
            arr.append(int(input()))
        
        matrix.append(arr)
        
    # for a in matrix:
    #     print(a)
    
    Saddle_price(matrix,n)