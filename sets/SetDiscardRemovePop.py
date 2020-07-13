if __name__ == '__main__':
    n = int(input())
    s = set(map(int, input().split()))

    for _ in range(int(input())):
        cmd = list(input().strip().split())
        if cmd[0] == 'remove':
            s.remove(int(cmd[1]))
        elif cmd[0] == 'discard':
            s.discard(int(cmd[1]))
        else:
            s.pop()

    print(sum(s))