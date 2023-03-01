def factorial(n):
    if(n==1):
        return 1
    
    fact1=factorial(n-1)
    f=n*fact1
    return f
    
    
    
if __name__ == '__main__':
    
    n=int(input())
    f2=factorial(n)
    print(f2)
    

