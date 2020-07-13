if __name__ == '__main__':

    from collections import OrderedDict
    od = OrderedDict()

    for _ in range(int(input())):
        w = input()
        od[w] = od.get(w,0) + 1

    print(len(od))
    print(*od.values())