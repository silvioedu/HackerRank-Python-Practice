if __name__ == '__main__':
    n, m = map(int, input().split())

    from collections import defaultdict
    d = defaultdict(list)

    for i in range(n):
        d[input()].append(i+1)

    for i in range(m):
        print(*d[input()] or [-1])
