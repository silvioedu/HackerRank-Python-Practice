if __name__ == '__main__':
    regex_pattern = r"[.,]+"
    import re
    print("\n".join(re.split(regex_pattern, input())))