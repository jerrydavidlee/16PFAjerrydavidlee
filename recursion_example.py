def factoria(n):
    if 1 == n:
        return 1
    else:
        return n*factoria(n-1)

    factoria(5)
    #call stack\
print(factoria(5))