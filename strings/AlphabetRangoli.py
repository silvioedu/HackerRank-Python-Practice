import string

def print_rangoli(size):
    alphabet = string.ascii_lowercase
    list_rangoli = []
    for i in range(n):
        s = "-".join(alphabet[i:n])
        list_rangoli.append((s[::-1]+s[1:]).center(4*n-3, "-"))

    print('\n'.join(list_rangoli[:0:-1]+list_rangoli))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)