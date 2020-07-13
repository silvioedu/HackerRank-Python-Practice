if __name__ == '__main__':
    from itertools import combinations

    N = int(input())
    L = input().split()
    K = int(input())

    li = list(combinations(L, K))
    fi = filter(lambda c: 'a' in c, li)

    print("{0:.3}".format(len(list(fi))/len(li)))