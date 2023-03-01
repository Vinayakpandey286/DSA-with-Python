def spiral_display(matrix,row,col):
    
    min_row=0
    max_row=row-1
    min_col=0
    max_col=col-1
    
    total_ele=row*col
    count=1
    
    while(count<=total_ele):
        if(count<=total_ele):
            for i in range(min_row,max_row+1):
                print(matrix[i][min_col])
                
                count+=1
            min_col+=1
        
        if(count<=total_ele):
            for i in range(min_col,max_col+1):
                print(matrix[max_row][i])
                
                count+=1
            max_row-=1
            
        if(count<=total_ele):
            for i in reversed(range(min_row,max_row+1)):
                print(matrix[i][max_col])
                
                
                count+=1
            max_col-=1
            
        if(count<=total_ele):
            for i in reversed(range(min_col,max_col+1)):
                print(matrix[min_row][i])
                
                count+=1
            min_row+=1            
    
    
if __name__ == '__main__':
    row=int(input())
    col=int(input())
    
    matrix=[]
    
    for i in range(row):
        arr=[]
        for j in range(col):
            arr.append(int(input()))
        matrix.append(arr)
    spiral_display(matrix,row,col)