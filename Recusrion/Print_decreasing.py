def print_decreasing(n):
    if (n==0):
        return
    print(n)
    print_decreasing(n-1)

if __name__ == '__main__':
    n=int(input())
    print_decreasing(n)