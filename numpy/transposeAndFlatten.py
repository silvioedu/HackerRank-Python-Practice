import numpy as np

if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = np.array([input().strip().split() for _ in range(n)], int)
    print(arr.transpose())
    print(arr.flatten())

