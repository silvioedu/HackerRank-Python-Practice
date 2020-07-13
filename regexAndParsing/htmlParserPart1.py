from abc import ABC
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser, ABC):
    def handle_starttag(self, tag, attrs):
        print('Start :', tag)
        for i in attrs:
            print('->', i[0], '>', i[1])

    def handle_endtag(self, tag):
        print('End   :', tag)

    def handle_startendtag(self, tag, attrs):
        print('Empty :', tag)
        for i in attrs:
            print('->', i[0], '>', i[1])


if __name__ == '__main__':
    parser = MyHTMLParser()
    [parser.feed(input()) for _ in range(int(input()))]
    parser.close()

