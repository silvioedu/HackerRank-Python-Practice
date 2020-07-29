import numpy as np

if __name__ == '__main__':
    n, m = map(int, input().split())
    a, b = (np.array([input().split() for _ in range(n)], dtype=int) for _ in range(2))
    print(np.add(a, b))
    print(np.subtract(a, b))
    print(np.multiply(a, b))
    print(np.array(np.divide(a, b), float))
    print(np.mod(a, b))
    print(np.power(a, b))

