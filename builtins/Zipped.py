if __name__ == '__main__':
    n, x = map(int, input().split())

    sheet = []
    [sheet.append(map(float, input().split())) for i in range(x)]

    for i in zip(*sheet):
        print(sum(i)/len(i))
