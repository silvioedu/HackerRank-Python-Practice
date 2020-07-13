from email.utils import parseaddr, formataddr
import re

if __name__ == '__main__':
    for _ in range(int(input())):
        email = parseaddr(input())
        if bool(re.search(r'^[a-zA-Z][\w\-.]*@[A-Za-z]+\.[a-zA-Z]{1,3}$', email[1])):
            print(formataddr(email))
