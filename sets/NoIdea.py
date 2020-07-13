if __name__ == '__main__':
    n,m = input().split()
    array = input().split()
    A,B = [set(input().split()) for _ in range(2)]
    print(sum([(i in A) - (i in B) for i in array]))
