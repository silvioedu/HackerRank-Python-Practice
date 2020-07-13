if __name__ == '__main__':

    from collections import namedtuple
    n = int(input())

    Student = namedtuple('Student',input().strip().split())
    print(sum(float(Student(*input().strip().split()).MARKS) for _ in range(n))/n)