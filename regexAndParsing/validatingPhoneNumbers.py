import re

if __name__ == '__main__':
    chk = {True: 'YES', False: 'NO'}
    p = '^[7-9]\d{9}$'
    for _ in range(int(input())):
        print(chk[bool(re.match(p, input()))])



