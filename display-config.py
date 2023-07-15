#!/home/ftc/Documents/FTC_Scoring_System/venv/bin/python

"""This program will configure a remote raspberry pi as a display. 

Build functionality for Schedule display, inspection display, pit display, and field timer."""

# Command: ssh pi@ftc-display-cgy3.local "echo 'http://ftc-scoring-cgy2.local' | sudo tee /boot/fullpageos.txt && sudo reboot"

"""
Will use a template JSON file to build a display config.
This script will be run as:
display-config ROLE
It will then browse for display records and prompt the user to select which device to configure.
Once chosen, it will prompt the user for relevant options and check those against choices
It will build a custom JSON from this information plus the end time and code for the event
It will then push this to the display using scp and trigger a display.py command 
"""

import argparse
from lib.display_manager import Display_Manager
from lib.event_manager import Event_Manager


arg_parser = argparse.ArgumentParser(add_help="This program will configure a display for the FTC Scoring System.")
arg_parser.add_argument("role", help="Type of Display. audience, pit, field, or inspect", type=str)
arg_parser.add_argument("-H", "--hostname", help="Hostname of the display, if already known", required=False)
arg_parser.add_argument("-C", "--eventcode", help="Event Code if already known", required=False)
args = arg_parser.parse_args()
if args.role not in ["audience", "pit", "field", "inspect"]:
    print("Invalid Role to configure: {}. Please provide a valid role. Run display-config.py -h for help.")
    exit(1)

display_manager = Display_Manager()
if args.hostname is None:
    print("These are the available displays to configure:")
    display_manager.print_Displays()
    hostname = display_manager.get_Hostname()
elif not display_manager.hostname_Valid(args.hostname):
    hostname = display_manager.get_Hostname()
else:
    hostname = args.hostname

event_manager = Event_Manager()
if args.eventcode is None:
    print("These are the available events to assign to:")
    event_manager.print_Events()
    eventcode = event_manager.get_Event_Code()
elif not event_manager.event_Code_Valid(args.eventcode):
    eventcode = event_manager.get_Event_Code()
else:
    eventcode = args.eventcode

print("Configuring {} as {} for event: {}.".format(hostname, args.role, eventcode))




