#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- by Alex -*-

import json
import bs4
import requests

class ParseCountry(object):

    country = ""

    def get_country(self, location):

        loc = location
        list_of_countries = (json.dumps(
            [
                {
                    ['name', 'alpha_2', 'alpha_3', 'numeric'][no]:
                    td.find_all()[-1].text
                    for no, td in enumerate(row.find_all('td')[:-1])
                }
                for row in bs4.BeautifulSoup(
                    requests.get('http://en.wikipedia.org/wiki/ISO_3166-1').text,
                    "lxml").find('table', {'class': 'wikitable sortable'}).find_all('tr')[1:]
            ],
            indent=4,
            ensure_ascii=False
        ))

        data = json.loads(list_of_countries)
        for i in range(len(list_of_countries)):
            elem1 = data[i]['name']
            if elem1 == loc:
                self.country = elem1
                break

        return self.country

    # def get_usa_state(self):
    #
    #     usa = 'usa'
    #
    #     return usa
    #     pass
