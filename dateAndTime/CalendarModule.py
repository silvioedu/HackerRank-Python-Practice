if __name__ == '__main__':
    import calendar as cal
    m, d, y = map(int, input().split())
    print(cal.day_name[cal.weekday(y, m, d)].upper())