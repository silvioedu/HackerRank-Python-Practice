if __name__ == '__main__':
    S,k = input().split()

    from itertools import permutations
    for i in permutations(sorted(S),int(k)):
        print("".join(i))
