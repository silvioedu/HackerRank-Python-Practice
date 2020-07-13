if __name__ == '__main__':
    for _ in range(int(input())):
        a,A = int(input()),set(map(int,input().split()))
        b,B = int(input()),set(map(int,input().split()))
        print(A.issubset(B))
