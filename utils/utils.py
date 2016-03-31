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

