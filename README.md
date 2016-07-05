# SensorE16

### Overview
SensorE16 is a bitcoin payable web app designed for the 21 Marketplace to allow users to sell temperature readings from their local environment.  

SensorE16 inspired by the Sensor21 project that allows grid computer operators to sell stats around temperature and barometric pressure from
sensors on their 21 computer.  That project requires a 21 Computer or Raspberry Pi and a breakout board, which is a bit of a high barrier to
entry for anyone just getting started.

In contrast, SensorE16 is targeted to use a USB temperature probe that can be used on any computer running the 21 platform.  Specifically,
it is built on the TEMPer USB temperature probe and uses the temper-python library to interact with it in the background.

### Setup

First, you will need a TEMPer USB temperature probe.  The one used for development was from Amazon.com and cost approx $15.  https://www.amazon.com/gp/product/B009YRP906/ref=oh_aui_search_detailpage?ie=UTF8&psc=1

Second, you will need to follow the instructions on the temper-python github project page to install the libraries.  You will also need to
follow the instructions to set the USB permissions so that non-root users can access the device.
https://github.com/padelt/temper-python

Finally, you will need to clone this repo to your device and run the server.
