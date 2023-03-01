def print_Increasing(n):
    if (n==0):
        return
    print_Increasing(n-1)
    print(n)

if __name__ == '__main__':
    n=int(input())
    print_Increasing(n)