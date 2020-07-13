from cmath import polar

if __name__ == '__main__':
    z = complex(input())
    polar = polar(z)
    print(polar[0])
    print(polar[1])