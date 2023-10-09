from .display import Display
from .common.utilities import Move_File_Contents_to_Remote_Host

class Sponsor_Display(Display):
    def __init__(self, hostname, role, ip_address, event_code):
        
        super().__init__(hostname, role, ip_address, event_code)
        self.url = "http://{host}:8080/event/{code}/display/?type=sponsor"

    def Apply_Config(self, config: dict):
        self.server = self.apply_server_name(config["server_ip"])
        self.completed_url = self.url.format(host=self.server, code=self.event_code)
        print(self.completed_url)
        Move_File_Contents_to_Remote_Host(self.completed_url, "/boot/fullpageos.txt", self.hostname)
        self.apply_Service_File()
