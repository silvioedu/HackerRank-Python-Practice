if __name__ == '__main__':
    n = int(input())
    m = input().split()
    print(all([int(i) > 0 for i in m]) and any([j == j[::-1] for j in m]))
