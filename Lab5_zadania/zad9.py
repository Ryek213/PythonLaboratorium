def fibonacchi(n):
    if n > 2:
        return fibonacchi(n-1) + fibonacchi(n-2)
    else:
        return 1


for i in range(1, 10):
    print(fibonacchi(i))
