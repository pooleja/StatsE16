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

__all__ = ["sensorE16"]


def sensorE16():
    """ runs ping against the url.

    Raises:
        ValueError: if the url is malformed or ping cannot be performed on it.
    Returns:
        dict: A dictionary containing ping information.

    """

    try:
        out = subprocess.check_output(['temper-poll']).decode('unicode_escape')
    except subprocess.CalledProcessError:
        raise ValueError("Temperature query failed for cmd: \"temper-poll\"")
    res = [line for line in out.split('\n') if line != '']
    info = {
        'temperature': res[1].split(' ')[2].split(u'\u00C2')[0],
        'timestamp': str(datetime.datetime.now())
    }
    return info

if __name__ == '__main__':
    data = sensorE16()
    formatted_data = json.dumps(data, indent=4, sort_keys=True)
    print(formatted_data)
