#!/home/ftc/Documents/FTC_Scoring_System/venv/bin/python

import pycurl
from io import BytesIO
import json
import requests
from pathlib import Path
import os
import argparse
from lib.common.utilities import Run_Cmd


"""This program is meant to update the FTC Scorekeeper software if necessary.

Program Flow:
1. Get the latest release info from Github (Done)
2. Compare the version number to the one currently installed
3. Download the new Software to ~/Downloads (Done)
4. Install the software in /usr/local/src
"""

__SCOREKEEPER_RELEASE_URL__ = "https://api.github.com/repos/FIRST-Tech-Challenge/scorekeeper/releases/latest"
__INSTALL_LOCATION__ = Path("/usr/local/src/scorekeeper")

def _get_Scorekeeper_Release_Info() -> dict:
    """This function fetches the latest release tag 
       and download URL of scorekeeper from Github
    """
    # Setup the Bytes and Curl objects for interacting with the Github API
    bytes_obj = BytesIO()
    curler = pycurl.Curl()
    curler.setopt(curler.URL, __SCOREKEEPER_RELEASE_URL__)
    curler.setopt(curler.WRITEDATA, bytes_obj)

    # Request the Information from Github and close the session
    curler.perform()
    curler.close()

    # Convert the output to a JSON dictionary
    release_info_dict = json.loads(bytes_obj.getvalue().decode('utf8'))

    # Get release tag to compare versions
    release_tag = release_info_dict['tag_name']

    # get download url
    download_url = release_info_dict['assets'][0]['browser_download_url']

    return {"Version": release_tag, "URL": download_url}

def download_Scorekeeper(url: str) -> Path:
    """This function downloads the newest scorekeeper zip"""
    temp_dir = Path("/tmp/scoring")
    if not temp_dir.exists():
        os.mkdir(str(temp_dir))
    filename = str(temp_dir / "scorekeeper.zip")
    download_request = requests.get(url, allow_redirects=True)

    with open(filename, 'wb') as file:
        file.write(download_request.content)

    return temp_dir / "scorekeeper.zip"

def install_Scorekeeper(zip_path: Path, version: str):
    """This function will uncompress the zip folder 
    and install it in __INSTALL_LOCATION__."""
    if not __INSTALL_LOCATION__.exists():
        if not __INSTALL_LOCATION__.is_dir():
            print("The install location is not a directory!")
            return False
        os.mkdir(str(__INSTALL_LOCATION__))
    else:
        os.system("rm -rf {}/*".format(__INSTALL_LOCATION__))
    if not zip_path.exists() or not zip_path.is_file():
        print("The Zip file does not exist or is not a file")
        return False
    os.system("unzip {} -d {}".format(zip_path, zip_path.parent))
    for item in zip_path.parent.iterdir():
        if item.is_dir():
            os.system("mv {}/* {}/".format(str(item), str(__INSTALL_LOCATION__)))
    with open(str(__INSTALL_LOCATION__ / "version.txt"), "w") as version_file:
        version_file.write(version)
    return True

def _check_For_Newer_Scorekeeper():
    release_info = _get_Scorekeeper_Release_Info()
    new_version = release_info["Version"].split('v')[1].split('.')
    for digit in new_version:
        digit = int(digit)
    try:
        with open(str(__INSTALL_LOCATION__ / "version.txt"), "r") as version_file:
            old_version = version_file.read().split('v')[1].split('.')
    except:
        return release_info
    for digit in old_version:
        digit = int(digit)
    if new_version[0] > old_version[0]:
        return release_info
    elif new_version[1] > old_version[1]:
        return release_info
    elif new_version[2] > old_version[2]:
        return release_info
    else:
        return None
    


#### Code Entry ####

arg_parser = argparse.ArgumentParser(add_help="This program aids setup of the FTC Scoring System.")
arg_parser.add_argument("cmd", help="Command. start, stop, update, or restart", type=str)
args = arg_parser.parse_args()
if args.cmd == "start":
    Run_Cmd("sudo systemctl start scorekeeper")
elif args.cmd == "stop":
    Run_Cmd("sudo systemctl stop scorekeeper")
elif args.cmd == "restart":
    Run_Cmd("sudo systemctl restart scorekeeper")
elif args.cmd == "update":
    Run_Cmd("sudo systemctl stop scorekeeper")
    release_info = _check_For_Newer_Scorekeeper()
    if not release_info:
        print("Scorekeeper is already the newest version!")
    else:
        zip_path = download_Scorekeeper(release_info["URL"])
        status = install_Scorekeeper(zip_path, release_info["Version"])
        print("Installation {} successful!".format("was" if status is True else "wasn't"))
    Run_Cmd("sudo systemctl start scorekeeper")
else:
    print("Please provide a valid command.")