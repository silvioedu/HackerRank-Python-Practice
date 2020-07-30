import numpy as np

if __name__ == '__main__':
    n = list(map(float, input().split()))
    m = int(input())
    print(np.polyval(n, m))
