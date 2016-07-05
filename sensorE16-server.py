#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import logging
import psutil
import subprocess
import os
import yaml
import ipaddress

from flask import Flask
from flask import request

from two1.wallet.two1_wallet import Wallet
from two1.bitserv.flask import Payment

from sensorE16 import sensorE16

app = Flask(__name__)

# setup wallet
wallet = Wallet()
payment = Payment(app, wallet)

# hide logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


@app.route('/manifest')
def manifest():
    """Provide the app manifest to the 21 crawler.
    """
    with open('./manifest.yaml', 'r') as f:
        manifest = yaml.load(f)
    return json.dumps(manifest)


@app.route('/')
@payment.required(5)
def measurement():
    """ Queries the TEMPer thermometer and returns the value.

    Returns: HTTPResponse 200 with a json containing the temper info.
    HTTP Response 400 if there is an error reading the temp.
    """
    try:
        data = sensorE16()
        response = json.dumps(data, indent=4, sort_keys=True)
        return response
    except ValueError as e:
        return 'HTTP Status 400: {}'.format(e.args[0]), 400


if __name__ == '__main__':
    import click

    @click.command()
    @click.option("-d", "--daemon", default=False, is_flag=True,
                  help="Run in daemon mode.")
    def run(daemon, private):
        if daemon:
            pid_file = './sensorE16.pid'
            if os.path.isfile(pid_file):
                pid = int(open(pid_file).read())
                os.remove(pid_file)
                try:
                    p = psutil.Process(pid)
                    p.terminate()
                except:
                    pass
            try:
                p = subprocess.Popen(['python3', 'sensorE16-server.py'])
                open(pid_file, 'w').write(str(p.pid))
            except subprocess.CalledProcessError:
                raise ValueError("error starting sensorE16-server.py daemon")
        else:
            print("Server running...")
            app.run(host='0.0.0.0', port=6016)

    run()
