from bs4 import BeautifulSoup
import os

__author__='Pruthvi Kumar'
# 30 June 2019.
# pruthvikumar.123@gmail.com
# Scrape contents of a loaded webpage into a text file and store into a text file within sink.


class ScrapePage:

    def __init__(self, page_source, sink_file_name):
        super(ScrapePage, self).__init__()
        self.page_source = page_source
        self.sink_file_name = sink_file_name

    @staticmethod
    def __scrape_body(page_source):
        soup = BeautifulSoup(page_source, features='html.parser')
        body = soup.find('body')
        the_contents_of_body_without_body_tags = body.findChildren()
        return the_contents_of_body_without_body_tags

    def extractor(self):
        try:
            # create a sink if not already existing
            os.makedirs('{}/../sink'.format(os.path.dirname(__file__)), exist_ok=True)

            # Extract page contents using Soup.
            with open('{}/../sink/{}.txt'.format(os.path.dirname(__file__), self.sink_file_name), "a") as f:
                print(self.__scrape_body(self.page_source), file=f)

        except Exception as e:
            print('Failed to scrape contents into {} file. Stack trace to follow.'.format(self.sink_file_name))
            print(str(e))
