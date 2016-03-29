#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- by Alex -*-

import socket

class Utils():

    @staticmethod
    def get_system_env():

        ubuntu_alef_ip = '192.168.0.161'
        ubuntu_bet_ip = '172.25.60.76'

        system_hostname = socket.gethostname()

        if system_hostname == 'booch':
            return ubuntu_alef_ip
        else:
            return ubuntu_bet_ip
