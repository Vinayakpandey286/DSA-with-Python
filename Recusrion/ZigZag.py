def zigzag(n):
    if(n==0):
        return
    
    print(n,end=" ")
    zigzag(n-1)
    print(n,end=" ")
    zigzag(n-1)
    print(n,end=" ")

if __name__ == '__main__':
    n=int(input())
    zigzag(n)
    
    