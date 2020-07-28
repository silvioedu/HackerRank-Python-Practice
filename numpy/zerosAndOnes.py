import numpy as np

if __name__ == '__main__':
    nums = tuple(map(int, input().split()))
    print(np.zeros(nums, dtype = np.int))
    print(np.ones(nums, dtype = np.int))
