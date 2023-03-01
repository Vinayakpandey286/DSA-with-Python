def State_of_wakanada(matrix):
    for gap in range(n):
        i=0
        for j in range(gap,n):
            print(matrix[i][j])
            i+=1


if __name__ == '__main__':
    n=int(input())
    matrix=[]
    
    for i in range(n):
        arr=[]
        for j in range(n):
            arr.append(int(input()))
        
        matrix.append(arr)
    
    State_of_wakanada(matrix)