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

from ping21 import ping21, getHostname

app = Flask(__name__)

# setup wallet
wallet = Wallet()
payment = Payment(app, wallet)

# flag for allowing private ip pinging
ALLOW_PRIVATE = False

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
def ping():
    """ Runs ping on the provided url

    Returns: HTTPResponse 200 with a json containing the ping info.
    HTTP Response 400 if no uri is specified or the uri is malformed/cannot be pingd.
    """
    try:
        uri = request.args['uri']
    except KeyError:
        return 'HTTP Status 400: URI query parameter is missing from your request.', 400

    try:
        if ipaddress.ip_address(getHostname(uri)).is_private and not ALLOW_PRIVATE:
            return 'HTTP Status 403: Private IP scanning is forbidden', 403
    except ValueError:
        pass

    try:
        data = ping21(uri)
        response = json.dumps(data, indent=4, sort_keys=True)
        return response
    except ValueError as e:
        return 'HTTP Status 400: {}'.format(e.args[0]), 400


if __name__ == '__main__':
    import click

    @click.command()
    @click.option("-d", "--daemon", default=False, is_flag=True,
                  help="Run in daemon mode.")
    @click.option("-p", "--private",  default=False, is_flag=True,
                  help="Allow ping21 to ping private ips.")
    def run(daemon, private):
        if private:
            global ALLOW_PRIVATE
            ALLOW_PRIVATE = private
        if daemon:
            pid_file = './ping21.pid'
            if os.path.isfile(pid_file):
                pid = int(open(pid_file).read())
                os.remove(pid_file)
                try:
                    p = psutil.Process(pid)
                    p.terminate()
                except:
                    pass
            try:
                p = subprocess.Popen(['python3', 'ping21-server.py'])
                open(pid_file, 'w').write(str(p.pid))
            except subprocess.CalledProcessError:
                raise ValueError("error starting ping21-server.py daemon")
        else:
            print("Server running...")
            app.run(host='0.0.0.0', port=6002)

    run()
