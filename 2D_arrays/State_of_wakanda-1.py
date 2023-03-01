def path(matrix,row,col):
    for i in range(col):
        if(i==0 or i%2==0):
            for j in range(row):
                print(matrix[j][i])
                
        else:
            for k in reversed(range(row)):
                print(matrix[k][i])
            
    
if __name__ == '__main__':
    row=int(input())
    col=int(input())
    matrix=[]
    
    for i in range(row):
        arr=[]
        for j in range(col):
            arr.append(int(input()))
        
        matrix.append(arr)
    
    
    f=open("output.txt","w")
    f.write("vinayak is handsome")
    f.close()
            
    path(matrix,row,col)