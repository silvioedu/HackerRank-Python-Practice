import re

if __name__ == '__main__':
    vowels = "aeiou"
    consonants = "qwrtypsdfghjklzxcvbnm"
    matcher = re.findall(r"(?<=[%s])([%s]{2,})[%s]" % (consonants, vowels, consonants), input(), flags = re.I)
    print('\n'.join(matcher or ['-1']))
