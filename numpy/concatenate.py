import numpy as np

if __name__ == '__main__':
    n, m, p = map(int, input().split())

    arr1 = np.array([input().strip().split() for _ in range(n)], int)
    arr2 = np.array([input().strip().split() for _ in range(m)], int)

    print(np.concatenate((arr1, arr2), axis = 0))
