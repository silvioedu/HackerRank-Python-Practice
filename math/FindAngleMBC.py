import math as m

if __name__ == '__main__':
    ab,bc = (int(input()) for _ in range(2))
    M = m.sqrt(pow(ab,2)+pow(bc,2))
    theta = m.acos(bc/M)
    print(str(round(m.degrees(theta)))+'°')
