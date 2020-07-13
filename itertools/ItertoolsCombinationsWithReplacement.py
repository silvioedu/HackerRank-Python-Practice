if __name__ == '__main__':
    S,k = input().split()

    from itertools import combinations_with_replacement
    for j in combinations_with_replacement(sorted(S),int(k)):
        print("".join(j))
