#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import platform
import requests
import shutil
import subprocess
import sys
from urllib.parse import urlparse

__all__ = ["ping21", "getHostname"]

def getHostname(uri):
    """ Cleans a provided uri

    Returns:
        str: cleaned uri

    """
    hostname = urlparse(uri).hostname
    if hostname is not None:
        return hostname

    return uri

def is_compatible():
    """ Checks whether the current machine is capable of running ping21

    Returns:
        bool: True if the machine is compatible false if not.

    """
    # check for Windows
    if hasattr(sys, 'getwindowsversion'):
        print('error: Windows is currently not supported.')
        return False

    # check for command presence
    if not shutil.which('ping'):
        print('error: Missing `ping` binary.')
        return False

    return True


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

def ping21(uri, num_packets=3, packet_size=64, wait_timeout=3.0):
    """ runs ping against the url.

    Args:
        url (str): A url to run ping against.

    Raises:
        ValueError: if the url is malformed or ping cannot be performed on it.
    Returns:
        dict: A dictionary containing ping information.

    """
    hostname = getHostname(uri)

    if not is_compatible():
        return

    if platform.system() == 'Darwin':
        wait_timeout = wait_timeout * 1000

    try:
        out = subprocess.check_output(['ping', '-c', str(num_packets),
            '-s', str(packet_size), '-W', str(wait_timeout), str(hostname)]
        ).decode('unicode_escape')
    except subprocess.CalledProcessError:
        raise ValueError("ping cannot be performed on url={}".format(hostname))
    res = [line for line in out.split('\n') if line != '']
    info = {
        'ping': res,
        'server': get_server_info()
    }
    return info

if __name__ == '__main__':
    url = sys.argv[1]
    data = ping21(url)
    formatted_data = json.dumps(data, indent=4, sort_keys=True)
    print(formatted_data)
