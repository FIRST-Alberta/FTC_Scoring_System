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
from lib.common.utilities import Get_Valid_Info


arg_parser = argparse.ArgumentParser(add_help="This program will configure a display for the FTC Scoring System.")
arg_parser.add_argument("role", help="Type of Display. audience, pit, field, or inspect", type=str)
arg_parser.add_argument("-H", "--hostname", help="Hostname of the display, if already known", required=False)
arg_parser.add_argument("-c", "--eventcode", help="Event Code if already known", required=False)
args = arg_parser.parse_args()
if args.role not in ["audience", "pit", "field", "inspect"]:
    print("Invalid Role to configure: {}. Please provide a valid role. Run display-config.py -h for help.")
    exit(1)

display_manager = Display_Manager()
if args.hostname is None:
    print("These are the available displays to configure:")
    display_manager.print_Displays()
    hostname = Get_Valid_Info("Which Hostname would you like to configure?", display_manager.displays)
elif args.hostname not in display_manager.displays:
    hostname = Get_Valid_Info("Which Hostname would you like to configure?", display_manager.displays)
else:
    hostname = args.hostname

event_manager = Event_Manager()
if args.eventcode is None:
    print("These are the available events to assign to:")
    event_manager.print_Events()
    eventcode = Get_Valid_Info("Which Eventcode would you like to use?", event_manager.events.keys())
elif args.eventcode not in event_manager.events.keys():
    eventcode = Get_Valid_Info("Which Eventcode would you like to use?", event_manager.events.keys())
else:
    eventcode = args.eventcode

print("Configuring {} as {} for event: {}.".format(hostname, args.role, eventcode))

# Now to build the config
new_display = Display_Manager.


