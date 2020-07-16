import xml.etree.ElementTree as etree

max_depth = -1


def depth(elem, level):
    global max_depth
    if level == max_depth:
        max_depth += 1

    for child in elem:
        depth(child, level + 1)


if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml = xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(max_depth)
