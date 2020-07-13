if __name__ == '__main__':
    from collections import Counter
    [print(*c) for c in Counter(sorted(input())).most_common(3)]
