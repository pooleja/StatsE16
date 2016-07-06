#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import platform
import requests
import shutil
import subprocess
import sys
import datetime
from urllib.parse import urlparse

__all__ = ["statsE16"]

def get_server_info():
    """Gets network metadata for the machine calling the function.
    see http://ipinfo.io for more info.
    Returns:
        dict: A dictionary with keys ip, hostname, city, region, country, loc, org, postal
    """
    uri = 'http://ipinfo.io'
    raw = requests.get(uri)
    data = raw.json()
    return data

def statsE16():
    """ Gets stats about the device.

    Raises:
        ValueError: if the location info or local device info cannot be discovered.
    Returns:
        dict: A dictionary containing device info.

    """

    info = {
        'server': get_server_info(),
        'cpu_cores': '0',
        'cpu_usage': '0',
        'memory_gb': '0',
        'memory_used': '0',
        'total_disk_space': '0',
        'disk_space_used': '0',
        'OS': '0',
    }
    return info

if __name__ == '__main__':
    data = statsE16()
    formatted_data = json.dumps(data, indent=4, sort_keys=True)
    print(formatted_data)
