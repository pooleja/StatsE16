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
To get paid for providing your stats, get it up and running, join the market, and then register your ZeroTier IP address with eSixteen.co.

To join the market:
```
$ 21 market join
```

## Register
Register your node with [E16](https://www.esixteen.co/register) to become part of the stats gathering pool.