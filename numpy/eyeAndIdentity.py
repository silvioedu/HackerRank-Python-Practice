import numpy as np

if __name__ == '__main__':
    dim = tuple(map(int, input().split()))
    np.set_printoptions(sign=' ')
    print(np.eye(dim[0], dim[1]))