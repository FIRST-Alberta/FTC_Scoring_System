#!/bin/env python3

from lib.common.utilities import Run_Cmd

# Flow
# 1. Get input for event code
# 2. Publish Record using avahi-publish -s event_code _http._tcp 8080

event_code = input("Please enter the event code and press enter:")

Run_Cmd(f"avahi-publish -s {event_code} _http._tcp 8080")