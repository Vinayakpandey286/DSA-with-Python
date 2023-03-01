def Exit_point(matrix,row,col):
    direction=0 # 0-east, 1-S,2-W,3-N
    i=0
    j=0
    
    while(True):
        direction=(direction+matrix[i][j])%4 # to keep dire b/w 0 to 3
        
        if(direction==0):
            j+=1
        elif(direction==1):
            i+=1
        elif(direction==2):
            j-=1
        elif(direction==3):
            i-=1
        
        if(i<0):
            i+=1
            break
        elif(j<0):
            j+=1
            break
        elif(i==row):
            i-=1
            break
        elif(j==col):
            j-=1
            break
        
    print(i)
    print(j)
if __name__ == '__main__':
    row=int(input())
    col=int(input())
    
    matrix=[]
    
    for i in range(row):
        arr=[]
        for j in range(col):
            arr.append(int(input()))
        matrix.append(arr)
        
    Exit_point(matrix,row,col)