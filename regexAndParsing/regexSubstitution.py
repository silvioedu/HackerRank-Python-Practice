import re


def substitution(s):
    s = re.sub(r' &&(?= )', ' and', s)
    s = re.sub(r' \|\|(?= )', ' or', s)
    return s


if __name__ == '__main__':
    for _ in range(int(input())):
        print(substitution(input()))
