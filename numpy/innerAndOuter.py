import numpy as np

if __name__ == '__main__':
    a = np.array(input().split(), int)
    b = np.array(input().split(), int)
    print(np.inner(a, b))
    print(np.outer(a, b))
