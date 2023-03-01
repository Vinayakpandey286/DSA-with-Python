def power_log(x,n):
    if(n==0):
        return 1
        
    xnb2=power_log(x,n//2)
    xn=xnb2*xnb2
    
    if(n%2==1):
        xn=xn*x
        
    return xn

if __name__ == '__main__':
    x=int(input())
    n=int(input())
    val=power_log(x,n)
    print(val)
    