cube = lambda x: pow(x,3)

def fibonacci(n):
    fib = [0,1]
    [fib.append(fib[i-2] + fib[i-1]) for i in range(2,n)]
    return(fib[0:n])

if __name__ == '__main__':
    n = int(input())
    print(map(cube, fibonacci(n)))