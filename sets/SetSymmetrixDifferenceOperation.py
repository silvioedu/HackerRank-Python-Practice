if __name__ == '__main__':
    n,sn = int(input()), set(input().split())
    b,sb = int(input()), set(input().split())
    print(len(sn.symmetric_difference(sb)))