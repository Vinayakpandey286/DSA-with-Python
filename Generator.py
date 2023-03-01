def gen(n):
    for i in range(n):
        yield i

g= gen(1000000)
for x in g:
    print(x)