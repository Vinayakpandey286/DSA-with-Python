def Tower_of_hanoi(n,t1,t2,t3):
    if(n==0):
        return

    Tower_of_hanoi(n-1,t1,t3,t2)
    print(n,end="")
    print(f"[{t1} -> {t2}]")
    Tower_of_hanoi(n-1,t3,t2,t1)

if __name__ == '__main__':
    
    n=int(input())
    t1=int(input())
    t2=int(input())
    t3=int(input())
    Tower_of_hanoi(n,t1,t2,t3)