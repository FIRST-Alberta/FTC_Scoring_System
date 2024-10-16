#!/bin/env python3

from lib.common.mdns_interface import MDNS_Interface
from lib.common.utilities import Run_Cmd
from ipaddress import IPv4Address


# this script will run on each display at boot.
# Flow:
# 1. Browse for a _http._tcp record made by the server.
# 2. Create the URL for the display based on this
#       "http://{host}:8080/event/{code}/display/?type=audience&{options}"
# 3. Set the URL to the kiosk

#Step 1
mdns_int = MDNS_Interface("_http._tcp","avahi.browse -trp")
mdns_int.browse()
event_code = ""
ip = None
for record in mdns_int.records:
    if record.port =="8080":
        ip = record.IP
        event_code = record.name
hostname = Run_Cmd("hostname")

#Step 2
if ip and event_code:
    url = f"http://{str(ip)}:8080/event/{event_code}/display/?type=audience&"
    url += "bindToField=all&"
    url += "scoringBarLocation=bottom&"
    url += "allianceOrientation=standard&"
    url += "liveScores=true&"
    url += "mute=true&" 
    url += "fieldStyleTimer=true&"
    url += "rankingsFontSize=larger&"
    url += f"name={hostname}"
else:
    third_octet = Run_Cmd("ip -4 addr show dev eth0 | grep inet").split()[1].split("/")[0].split(".")[2]
    ip = f"192.168.{third_octet}.10"
    url = f"http://{ip}:8080"

#Step 3
Run_Cmd(f"snap set wpe-webkit-mir-kiosk url={url}", timeout=30)


