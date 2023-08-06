from .event import Event
from datetime import datetime
from common.utilities import Get_Valid_Info

__DISPLAY_URL__ = "http://{host}.local/event/{code}/display/?{}"
__INSPECTION_STATUS_URL__ = "http://{host}.local/event/{code}/status/proj/{col}"

___DISPLAY_OPTIONS__ = {"type": ["pit", "sponsor", "audience", "field"],
                        "colomns": ["1", "2", "3"],
                        "bindToField": ["all", "1", "2"],
                        "scoringBarLocation": ["bottom", "top"],
                        "allianceOrientation": ["standard", "flipped"],
                        "liveScores": ["true", "false"],
                        "mute": ["true", "false"],
                        "muteRandomizationResults": ["true", "false"],
                        "fieldStyleTimer": ["true", "false"],
                        "overlay": ["true", "false"],
                        "overlayColor": {"green": "%2300FF00",
                                         "pink": "%23FF00FF"},
                        "allianceSelectionStyle": ["classic", "hybrid"],
                        "awardsStyle": ["classic", "overlay"],
                        "previewStyle": ["classic", "overlay"],
                        "randomStyle": ["classic", "overlay"],
                        "dualDivisionRankingStyle": "sideBySide",
                        "rankingsFontSize": ["larger", "smaller"],
                        "rankingsShowQR": ["true", "false"],
                        "showMeetRankings": ["true", "false"],
                        "rankingsAllTeams": ["true", "false"]}


class Display:
    def __init__(self, hostname: str):
        self.display_hostname = hostname
        self.server_hostname = None
        self.display_type = None
        self.display_url = None
        self.config_info = {}

    def config_Audience(self):

        return
    
    def config_Pit(self):
        # "rankingsFontSize": ["larger", "smaller"],
        # "rankingsShowQR": ["true", "false"],
        return
    
    def config_Inspect(self):
        # Num of coloumns
        print("The inspection status board supports 1, 2 or 3 colomns.")
        self.config_info["colomns"] = Get_Valid_Info("How many coloumns would you like?",
                                                     ___DISPLAY_OPTIONS__["colomns"])
        return
    
    def config_Field(self):
        return

    def Build_Config(self, server_hostname, event: Event, role: str):
        self.config_info["server"] = server_hostname
        self.config_info["type"] = role
        self.config_info["eventcode"] = event.code
        self.config_info["expiry"] = event.end + datetime.timedelta(days=1)

        if role == "inspect":
            self.config_Inspect()
        elif role == "pit":
            self.config_Pit()
        elif role == "field":
            self.config_Field()
        elif role == "audience":
            self.config_Audience()
        else:
            print("Invalid Role")
            exit(1)
        


