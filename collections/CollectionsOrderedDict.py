if __name__ == '__main__':

    from collections import OrderedDict
    od = OrderedDict()

    for _ in range(int(input())):
        items = input().rpartition(" ")
        od[items[0]] = od.get(items[0],0) + int(items[2])

    for item, quantity in od.items():
        print(item, quantity)
