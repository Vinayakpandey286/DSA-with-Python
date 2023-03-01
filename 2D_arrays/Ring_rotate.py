def ring_rotate(matrix,r,s):
    oned=fillonedfrommatrix(matrix,s)
    rotate(oned,r)
    fillshellfromoned(matrix,s,oned)
    
def fillonedfrommatrix(matrix,s):
    minr=s-1
    minc=s-1
    maxr=len(matrix)-s
    maxc=len(matrix[0])-s
    size=2*(maxr-minr)+2*(maxc-minc)
    oned=[0]*size
    
    index=0
    for i in range(minr,maxr+1):
        j=minc
        oned[index]=matrix[i][j]
        index+=1
        
    for i in range(minc+1,maxc+1):
        j=maxr
        oned[index]=matrix[j][i]
        index+=1
        
    for i in reversed(range(minr,maxr)):
        j=maxc
        oned[index]=matrix[i][j]
        index+=1
    
    for i in reversed(range(minc+1,maxc)):
        j=minr
        oned[index]=matrix[j][i]
        index+=1
        
    return oned
    
def rotate(oned,r):
    r%=len(oned)
    if(r<0):
        r+=len(oned)
        
    reverse(oned,0,len(oned)-r-1)
    reverse(oned,len(oned)-r,len(oned)-1)
    reverse(oned,0,len(oned)-1)

def reverse(oned,i,j):
    while(i<j):
        temp=oned[i]
        oned[i]=oned[j]
        oned[j]=temp
        i+=1
        j-=1

def fillshellfromoned(matrix,s,oned):
    minr=s-1
    minc=s-1
    maxr=len(matrix)-s
    maxc=len(matrix[0])-s
    
    index=0
    for i in range(minr,maxr+1):
        j=minc
        matrix[i][j]=oned[index]
        index+=1
        
    for i in range(minc+1,maxc+1):
        j=maxr
        matrix[j][i]=oned[index]
        index+=1
        
    for i in reversed(range(minr,maxr)):
        j=maxc
        matrix[i][j]=oned[index]
        index+=1
    
    for i in reversed(range(minc+1,maxc)):
        j=minr
        matrix[j][i]=oned[index]
        index+=1
   
def display(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j],end=" ")
            
        print()

if __name__ == '__main__':
    row=int(input())
    col=int(input())
    
    matrix=[]
    
    for i in range(row):
        arr=[]
        for j in range(col):
            arr.append(int(input()))
        matrix.append(arr)

    s=int(input())
    r=int(input())
    
    ring_rotate(matrix,r,s)
    display(matrix)