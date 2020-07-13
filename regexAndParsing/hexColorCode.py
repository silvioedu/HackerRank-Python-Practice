import re


def isValid(s):
    brackets = ['{', '}']
    for i in brackets:
        if s.count(i) > 0 or s.count(':') == 0:
            return False
    return True


if __name__ == '__main__':
    for i in range(int(input())):
        s = input()
        if isValid(s):
            [print(i) for i in re.findall(r'#[a-fA-F0-9]{3,6}', s)]
