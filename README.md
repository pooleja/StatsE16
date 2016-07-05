# SensorE16

## Overview
SensorE16 is a bitcoin payable web app designed for the 21 Marketplace to allow users to sell temperature readings from their local environment.  

SensorE16 inspired by the Sensor21 project that allows grid computer operators to sell stats around temperature and barometric pressure from
sensors on their 21 computer.  That project requires a 21 Computer or Raspberry Pi and a breakout board, which is a bit of a high barrier to
entry for anyone just getting started.

In contrast, SensorE16 is targeted to use a USB temperature probe that can be used on any computer running the 21 platform.  Specifically,
it is built on the TEMPer USB temperature probe and uses the temper-python library to interact with it in the background.

## Setup

### Hardware

First, you will need a TEMPer USB temperature probe.  The [one used for development](https://www.amazon.com/gp/product/B009YRP906/ref=oh_aui_search_detailpage?ie=UTF8&psc=1)
was from Amazon.com and cost approx $15.

### USB Client software

Second, you will need to follow the instructions on the [temper-python github project page](https://github.com/padelt/temper-python) to
install the libraries.  You will also need to
follow the instructions to set the USB permissions so that non-root users can access the device.

Install the prerequisites (no need for SNMP):
```
sudo apt-get install python-usb python-setuptools
```

Clone the Lib:
```
git clone https://github.com/padelt/temper-python.git
```

Run the setup:
```
cd temper-python
sudo python setup.py install
```

Override USB device permissions (You may need to reboot after this):
```
sudo cp etc/99-tempsensor.rules /etc/udev/rules.d/
```

Ensure that the temperature probe is working correctly by running 'temper-poll' before contiuing:
```
$ temper-poll
Found 1 devices
Device #0: 27.5°C 81.5°F
```

### SensorE16

Finally, you will need to clone this repo to your device and get the server set up.
```
git clone https://github.com/pooleja/sensorE16.git
cd SensorE16
sudo easy_install3 pip
sudo pip3 install -r requirements.txt
./setup.sh
python3 sensorE16-server.py -d
```

## Testing
You should then be able test the endpoint by running a 21 buy command on the local machine for port 6016:
```
$ 21 buy http://127.0.0.1:6016
{
    "temperature": "27.6",
    "timestamp": "2016-07-05 16:36:32.893140"
}
You spent: 5 Satoshis. Remaining 21.co balance: XXXX Satoshis.
```
