if __name__ == '__main__':
    S = list(map(int,input()))

    from itertools import groupby
    for i,j in groupby(S):
        print(tuple([len(list(j)), i]),end=" ")
