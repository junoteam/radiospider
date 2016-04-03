#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- by Alex -*-

import socket

class Utils():

    # Here we get IP of machine that we work with
    @staticmethod
    def get_system_env():
        ubuntu_alef_ip = '192.168.0.161'
        ubuntu_bet_ip = '172.25.60.76'
        system_hostname = socket.gethostname()
        if system_hostname == 'booch':
            return ubuntu_alef_ip
        else:
            return ubuntu_bet_ip

    # Here we replace quotes in text in tweet or in any other string
    @staticmethod
    def replace_quots(text):
        text = str(text)
        replaced_quotes = ["'", '"']
        for char in replaced_quotes:
            text = text.replace(char, "\\" + char)

        if len(text) > 0:
            if text[:-1] == '\\':
                text[:-1] = ""
        return text

    # Only lists of states for USA & Canada
    @staticmethod
    def states_usa_list():
        states = {
            'AK': 'Alaska',
            'AL': 'Alabama',
            'AR': 'Arkansas',
            'AS': 'American Samoa',
            'AZ': 'Arizona',
            'CA': 'California',
            'CO': 'Colorado',
            'CT': 'Connecticut',
            'DC': 'District of Columbia',
            'DE': 'Delaware',
            'FL': 'Florida',
            'GA': 'Georgia',
            'GU': 'Guam',
            'HI': 'Hawaii',
            'IA': 'Iowa',
            'ID': 'Idaho',
            'IL': 'Illinois',
            'IN': 'Indiana',
            'KS': 'Kansas',
            'KY': 'Kentucky',
            'LA': 'Louisiana',
            'MA': 'Massachusetts',
            'MD': 'Maryland',
            'ME': 'Maine',
            'MI': 'Michigan',
            'MN': 'Minnesota',
            'MO': 'Missouri',
            'MP': 'Northern Mariana Islands',
            'MS': 'Mississippi',
            'MT': 'Montana',
            'NA': 'National',
            'NC': 'North Carolina',
            'ND': 'North Dakota',
            'NE': 'Nebraska',
            'NH': 'New Hampshire',
            'NJ': 'New Jersey',
            'NM': 'New Mexico',
            'NV': 'Nevada',
            'NY': 'New York',
            'OH': 'Ohio',
            'OK': 'Oklahoma',
            'OR': 'Oregon',
            'PA': 'Pennsylvania',
            'PR': 'Puerto Rico',
            'RI': 'Rhode Island',
            'SC': 'South Carolina',
            'SD': 'South Dakota',
            'TN': 'Tennessee',
            'TX': 'Texas',
            'UT': 'Utah',
            'VA': 'Virginia',
            'VI': 'Virgin Islands',
            'VT': 'Vermont',
            'WA': 'Washington',
            'WI': 'Wisconsin',
            'WV': 'West Virginia',
            'WY': 'Wyoming'
        }
        pass

    @staticmethod
    def states_canada_list():
        prov_terr = {
            'AB': 'Alberta',
            'BC': 'British Columbia',
            'MB': 'Manitoba',
            'NB': 'New Brunswick',
            'NL': 'Newfoundland and Labrador',
            'NT': 'Northwest Territories',
            'NS': 'Nova Scotia',
            'NU': 'Nunavut',
            'ON': 'Ontario',
            'PE': 'Prince Edward Island',
            'QC': 'Quebec',
            'SK': 'Saskatchewan',
            'YT': 'Yukon'
        }

        provinces = {
            'AB': 'Alberta',
            'BC': 'British Columbia',
            'MB': 'Manitoba',
            'NB': 'New Brunswick',
            'NL': 'Newfoundland and Labrador',
            'NS': 'Nova Scotia',
            'ON': 'Ontario',
            'PE': 'Prince Edward Island',
            'QC': 'Quebec',
            'SK': 'Saskatchewan'
        }

        territories = {
            'NT': 'Northwest Territories',
            'NU': 'Nunavut',
            'YT': 'Yukon'
        }
        pass


