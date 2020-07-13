def count_substring(string, sub_string):
    l_st = len(string)
    l_sbt = len(sub_string)
    count = 0
    for i in range(l_st - l_sbt + 1):
        if string[i:i+l_sbt] == sub_string:
            count += 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)