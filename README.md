# FTC_Scoring_System

This is a collection of scripts that will be built into software to implement a scoring system in a box that is mostly automated and user friendly

## Hardware Used

### Server
Intel NUC 11 with:
* Intel Celeron N5105 Quad Core 2GHz Processor
* 16 GB 3200 MHz SDRAM 
* 250 GB NVME Solid State Drive
* Ubuntu 22.04 LTS Operating System

### Network
* Router: D-Link AC3000 High Power Wi-Fi Tri Band Gigabit Mesh Router (DIR-3040)
* Booster(s): D-Link AC1200 Mesh Wi-Fi Range Extender (DAP-1610)

### Display
Raspberry Pi Zero Wireless with:
* Aluminium Case
* 32 GB Class 10 SD Card
* Dedicated 3A Power supply
* BrosTrend AC650 Long Range Dual Band Wi-Fi Adapter
* FullPageOS

## Server Setup
1. Install Ubuntu 22.04 with username ftc and password ftc
2. Install the [Raspberry Pi Imager](https://www.raspberrypi.com/software/).


### Package Requirements

* pip
    - pycurl
    - requests
* apt:
    - libssl-dev
    - libcurl4-openssl-dev
    - openjdk-18-jdk