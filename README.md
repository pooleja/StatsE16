# StatsE16

## Overview
StatsE16 is a bitcoin payable web app designed for the 21 Marketplace to allow users to sell statistics about the device they are running.  The goal is to use this service to understand what devices are running out there and the capacity of the network.  Also metadata such as Up-Time and capacity of individual nodes can be inferred.


## Setup

First, get the project and install dependencies.

```
$ git clone https://github.com/pooleja/StatsE16.git
$ cd StatsE16
$ sudo easy_install pip
$ sudo pip install -r requirements.txt
```

Next, verify it works.  This should output the JSON data showing you stats.
```
$ python3 statsE16.py

{
    "cpu_count": 4,
    "cpu_used_percent": 2.8,
    "disk_total": 125745487872,
    "disk_used_percent": 61.6,
    "memory_total": 1020764160,
    "memory_used_percent": 10.9,
    "platform_dist": "debian 8.0",
    "platform_release": "4.1.10-v7+",
    "platform_system": "Linux",
    "server": {
        "city": "Atlanta",
        "country": "US",
        "hostname": "108-234-94-217.lightspeed.tukrga.sbcglobal.net",
        "ip": "108.234.94.217",
        "loc": "33.7884,-84.3491",
        "org": "AS7018 AT&T Services, Inc.",
        "postal": "30306",
        "region": "Georgia"
    }
}
```

Finally, run it as a daemon to have the service ready for others to consume.
```
$ python3 statsE16-server.py -d
Server running...
```

## Get Paid
To get paid for providing your stats, get it up and running, join the market, and then send me your ZeroTier IP address.  You can DM it to me on Slack at https://slack.21.co.  My name is 'poole_party'.

To join the market:
```
21 market join
```

To get your ZeroTier IP:
```
$ sudo zerotier-cli listnetworks
```
You will see an output that looks similar to this:
```
200 listnetworks <nwid> <name> <mac> <status> <type> <dev> <ZT assigned ips>
200 listnetworks 6c0c6960a20bf150 21market 32:04:57:14:35:89 OK PRIVATE zt0 10.244.108.6/16
```
Locate the row that says 21 market and your IP address will be the number at the end of that line with the form 10.244.XXX.XXX (ignore the number following the slash).  In this example, the IP address is "10.244.108.6".
