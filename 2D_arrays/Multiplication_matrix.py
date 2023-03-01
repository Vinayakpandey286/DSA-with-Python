def Matrix_multipliation(Matrix1,Matrix2,row1,col1,row2,col2):
    if(col1==row2):
        Multmatrix=[[0 for i in range(col2)] for j in range(row1)]
        for i in range(row1):
            for j in range(col2):
                temp=0
                for k in range(row2):
                    temp+=Matrix1[i][k]*Matrix2[k][j]
                    
                Multmatrix[i][j]=temp
            
    else:
        print("Invalid input")
        
    for i in range(row1):
        for j in range(col2):
            print(Multmatrix[i][j],end=" ")
            
        print()
            
    
if __name__ == '__main__':
    
    row1=int(input())
    col1=int(input())
    
    Matrix1=[]
    
    for i in range(row1):
        arr=[]
        for j in range(col1):
            val=int(input())
            arr.append(val)
        Matrix1.append(arr)
    
    row2=int(input())
    col2=int(input())
    
    Matrix2=[]
    
    for i in range(row2):
        arr=[]
        for j in range(col2):
            val=int(input())
            arr.append(val)
        Matrix2.append(arr)
        
    #print(Matrix1)
    #print(Matrix2)
    
    Matrix_multipliation(Matrix1,Matrix2,row1,col1,row2,col2)
