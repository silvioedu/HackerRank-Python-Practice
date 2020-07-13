if __name__ == '__main__':
    S,k = input().split()

    from itertools import combinations
    for i in range(1, int(k)+1):
        for j in combinations(sorted(S),int(i)):
            print("".join(j))
