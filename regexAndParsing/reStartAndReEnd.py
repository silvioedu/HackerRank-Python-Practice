import re

if __name__ == '__main__':
    s = input()
    pattern = re.compile(input())
    m = pattern.search(s)

    if not m:
        print(tuple([1, -1]))

    while m:
        print(tuple([m.start(), m.end() - 1]))
        m = pattern.search(s, m.start() + 1)