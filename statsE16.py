#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import platform
import requests
import shutil
import subprocess
import sys
import datetime
import psutil
import platform
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
        'cpu_count': psutil.cpu_count(),
        'cpu_used_percent': psutil.cpu_percent(interval=1),
        'memory_total': psutil.virtual_memory().total,
        'memory_used_percent': psutil.virtual_memory().percent,
        'disk_total': psutil.disk_usage('/').total,
        'disk_used_percent': psutil.disk_usage('/').percent,
        'platform_system': platform.system(),
	'platform_release': platform.release(),
	'platform_dist': platform.dist()[0] + " " + platform.dist()[1]
    }
    return info

if __name__ == '__main__':
    data = statsE16()
    formatted_data = json.dumps(data, indent=4, sort_keys=True)
    print(formatted_data)
