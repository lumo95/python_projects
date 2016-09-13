# Name: Crawl
# Created By: Luke Molloy
# Date: 23/08/16
# Desc: A program that searches a website for links and titles on
# its pages


import requests
from bs4 import BeautifulSoup
import textwrap
import random


def forum_spider(max_pages):

    page = 1
    number = 0
    content_list = []

    while page < max_pages:
        url = 'https://thenewboston.com/forum/search_topics.php?page=' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text  # gets only the text in plain text format
        soup = BeautifulSoup(plain_text, "html.parser")

        for link in soup.findAll('a', {'class': 'title text-semibold'}):
            number += 1
            href = link.get('href')
            content = link.string
            dedent_text = textwrap.dedent(content).strip()
            x = str(number) + ') ' + 'Title: ' + dedent_text + '\n' + 'Link: ' + href + '\n'
            content_list.append(x)

        page += 1
        return content_list


def create_file():
    file_num = str(random.randint(0, 1000))
    file = open(file_num + '_new_crawl.txt', 'w')  # create the file and write to it with 'w'
    cont = forum_spider(max_pages=2)
    file.writelines("\n".join(cont))
    file.close()

create_file()
