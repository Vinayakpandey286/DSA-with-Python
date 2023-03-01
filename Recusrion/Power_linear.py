def power_linear(n,x):
    if(x==0):
        return 1
    
    temp=power_linear(n,x-1)
    power=n*temp
    return power
    
if __name__ == '__main__':
    
    n=int(input())
    x=int(input())
    temp1=power_linear(n,x)
    print(temp1)
    

