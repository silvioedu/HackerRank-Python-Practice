if __name__ == '__main__':
    N = int(input())

    list = []
    for _ in range(N):
        s = input().split(" ")

        cmd = s[0]
        if len(s) > 1:
            if (len(s) == 3):
                arg2 = int(s[2])
            arg1 = int(s[1])

        if cmd == "insert":
            list.insert(arg1,arg2)
        elif cmd == "remove":
            list.remove(arg1)
        elif cmd == "append":
            list.append(arg1)
        elif cmd == "sort":
            list.sort()
        elif cmd == "pop":
            list.pop()
        elif cmd == "reverse":
            list.reverse()
        else:
            print(list)
