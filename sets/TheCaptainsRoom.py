if __name__ == '__main__':
    k,members = int(input()),list(map(int, input().split()))
    membersset = set(members)
    print(((sum(membersset)*k)-(sum(members)))//(k-1))

