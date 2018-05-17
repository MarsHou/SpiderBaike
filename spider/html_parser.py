# -*- coding: utf-8 -*-
import re
from urllib.parse import urljoin

from bs4 import BeautifulSoup


class HtmlParser(object):
    def parse(self, new_url, html_content):
        if new_url is None or html_content is None:
            return

        soup = BeautifulSoup(html_content, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(new_url, soup)
        new_data = self._get_new_data(new_url, soup)
        return new_urls, new_data

    def _get_new_urls(self, page_url, soup):
        links = soup.find_all('a', href=re.compile(r"/item/"))
        new_urls = set()
        for link in links:
            new_url = link['href']
            new_full_url = urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, new_url, soup):
        res_data = {'url': new_url}

        title = soup.find('dd', class_='lemmaWgt-lemmaTitle-title')
        title_h1 = title.find('h1')
        title_h2 = title.find('h2')
        h2 = ""
        if not title_h2 is None:
            h2 = title_h2.get_text()
        res_data['title'] = title_h1.get_text() + h2

        summary_node = soup.find('div', class_='lemma-summary')
        res_data['summary'] = summary_node.get_text()

        return res_data
