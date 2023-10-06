from .display import Display

__DISPLAY_OPTIONS__ = {
                        "bindToField": ["all", "1", "2"],
                        "scoringBarLocation": ["bottom", "top"],
                        "allianceOrientation": ["standard", "flipped"],
                        "liveScores": [True, False],
                        "mute": [True, False],
                        "muteRandomizationResults": [True, False],
                        "fieldStyleTimer": [True, False],
                        "rankingsFontSize": ["larger", "smaller"]
                       }



class Field_Display(Display):
    def __init__(self, hostname, role, ip_address, event_code):
        self.url = "http://{host}:8080/event/{code}/display/?type=field&{}"
        super().__init__(hostname, role, ip_address, event_code)

    def Apply_Config(self, config: dict):
        self.apply_server_name(config["server_ip"])
        options = ""
        for option in __DISPLAY_OPTIONS__.keys():
            if isinstance(config[option + "-f"], bool):
                if config[option + "-f"]:
                    val = "true"
                else: val = "false"
            else: val = config[option + "-f"]
            options += "{}={}&".format(option, val)
        options += "name={}".format(self.hostname)
        self.completed_url = self.url.format(host=self.server, code=self.event_code, options=options)
        self.complete_Service_File()
