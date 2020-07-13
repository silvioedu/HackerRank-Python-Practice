if __name__ == '__main__':
    a = int(input())
    A = set(map(int, input().split()))

    for i in range(int(input())):
        s, b = input().split()
        if s == 'intersection_update':
            A.intersection_update(set(map(int, input().split())))
        elif s == 'update':
            A.update(set(map(int, input().split())))
        elif s == 'symmetric_difference_update':
            A.symmetric_difference_update(set(map(int, input().split())))
        else:
            A.difference_update(set(map(int, input().split())))

    print(sum(A))
