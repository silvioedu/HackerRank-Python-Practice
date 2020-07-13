if __name__ == '__main__':

    upper = []
    lower = []
    even  = []
    odd   = []

    for i in sorted(input()):
        if i.isalpha():
            if i.isupper():
                upper.append(i)
            else:
                lower.append(i)
        else:
            if int(i) % 2 == 0:
                even.append(i)
            else:
                odd.append(i)

    print("".join(lower+upper+odd+even))