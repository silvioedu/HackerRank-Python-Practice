if __name__ == '__main__':

    from collections import deque
    d = deque()

    for _ in range(int(input())):
        cmd = list(input().strip().split())
        if cmd[0] == 'append':
            d.append(cmd[1])
        elif cmd[0] == 'appendleft':
            d.appendleft(cmd[1])
        elif cmd[0] == 'pop':
            d.pop()
        else:
            d.popleft()

    print(*d)