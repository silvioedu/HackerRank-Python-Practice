if __name__ == '__main__':
    A,B = [list(map(int,input().split())) for _ in range(2)]

    from itertools import product
    print(*product(A,B))