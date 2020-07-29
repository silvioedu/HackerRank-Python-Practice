import numpy as np

if __name__ == '__main__':
    np.set_printoptions(sign=' ')
    a = np.array(input().split(), float)
    print(np.floor(a))
    print(np.ceil(a))
    print(np.rint(a))
