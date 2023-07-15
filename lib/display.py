

__DISPLAY_URL__ = "http://{host}.local/event/{code}/display/?{}"
__INSPECTION_STATUS_URL__ = "http://{host}.local/event/{code}/status/proj/{col}"

___DISPLAY_OPTIONS__ = {"type": ["pit", "sponsor", "audience", "field"],
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
    def __init__(self):
        self.display_hostname = None
        self.display_type = None
        self.display_url = None
        self.server_hostname = None

    def form_URL():
        return "http://"