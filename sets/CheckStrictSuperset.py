if __name__ == '__main__':
    A = set(input().split())
    print(all(A > set(input().split()) for _ in range(int(input()))))
