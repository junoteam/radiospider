#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- by Alex -*-

import json
import bs4
import requests

class ParseCountry(object):

    def __init__(self):
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

        self.countries_list = json.loads(list_of_countries)

    def get_country(self, location):

        country = ""
        location = location.lower()

        for i in range(len(self.countries_list)):
            elem1 = self.countries_list[i]['name']
            if elem1.lower() in location:
                country = elem1
                break
        return country

    # def get_usa_state(self):
    #
    #     usa = 'usa'
    #
    #     return usa
    #     pass
