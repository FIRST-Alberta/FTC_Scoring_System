from .display import Display
from .common.utilities import Move_File_Contents_to_Remote_Host


__DISPLAY_OPTIONS__ = {"rankingsFontSize": ["larger", "smaller"],
                        "rankingsShowQR": [True, False]
                        }


class Pit_Display(Display):
    def __init__(self, hostname, role, ip_address, event_code):
        
        super().__init__(hostname, role, ip_address, event_code)
        self.url = "http://{host}:8080/event/{code}/display/?type=pit&{options}"

    def Apply_Config(self, config: dict):
        self.server = self.apply_server_name(config["server_ip"])

        options = ""
        for option in __DISPLAY_OPTIONS__.keys():
            if isinstance(config[option + "-p"], bool):
                if config[option + "-p"]:
                    val = "true"
                else: val = "false"
            else: val = config[option + "-p"]
            options += "{}={}&".format(option, val)
        options += "name={}".format(self.hostname)
        self.completed_url = self.url.format(host=self.server, code=self.event_code, options=options)
        print(self.completed_url)
        Move_File_Contents_to_Remote_Host(self.completed_url, "/boot/fullpageos.txt", self.hostname)
        self.apply_Service_File()