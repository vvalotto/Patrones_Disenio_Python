
from urllib.request import urlopen


class AbstractNewsParser(object):

    def __init__(self):
        if self.__class__ is AbstractNewsParser:
            raise TypeError('No se puede instanciar')

    def print_top_news(self):
        url = self.get_url()
        raw_content = self.get_raw_content(url)
        content = self.parse_content(raw_content)

        cropped = self.crop(content)

        for item in cropped:
            print("Title ", item['title'])
            print("Content ", item['content'])
            print("Link ", item['link'])
            print("Published ", item['pucblished'])
            print("Id ", item['id'])

    def get_url(self):
        raise NotImplementedError()

    def get_raw_content(self, url):
        return urlopen(url)

