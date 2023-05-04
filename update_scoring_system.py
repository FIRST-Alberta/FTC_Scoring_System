import pycurl
from io import BytesIO
import json
import requests
from pathlib import Path

"""This program is meant to update the FTC Scorekeeper software if necessary.

Program Flow:
1. Get the latest release info from Github (Done)
2. Compare the version number to the one currently installed
3. Download the new Software to ~/Downloads (Done)
4. Install the software in /usr/local/src
"""

__SCOREKEEPER_RELEASE_URL__ = "https://api.github.com/repos/FIRST-Tech-Challenge/scorekeeper/releases/latest"

def get_Scorekeeper_Release_Info() -> dict:
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

def download_Scorekeeper(url: str, path: Path):
    """This function downloads the newest scorekeeper zip"""
    filename = str(path / "Scorekeeper.zip")
    download_request = requests.get(url, allow_redirects=True)

    with open(filename, 'wb') as file:
        file.write(download_request.content)


#### Code Entry ####
release_info = get_Scorekeeper_Release_Info()
print("Release Tag: ", release_info["Version"])
print("Download URL: ", release_info["URL"])
download_Scorekeeper(release_info["URL"], Path("/home/ftc/Downloads"))