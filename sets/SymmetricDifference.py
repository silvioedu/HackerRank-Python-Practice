if __name__ == '__main__':
    a,b = [set(input().split()) for _ in range(4)][1::2]
    print(*sorted(a^b, key=int), sep='\n')

