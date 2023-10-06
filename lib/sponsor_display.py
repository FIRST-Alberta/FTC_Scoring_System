from .display import Display

class Sponsor_Display(Display):
    def __init__(self, hostname, role, ip_address, event_code):
        self.url = "http://{host}:8080/event/{code}/display/?type=sponsor"
        super().__init__(hostname, role, ip_address, event_code)

    def Apply_Config(self, config: dict):
        self.apply_server_name(config["server_ip"])
        self.completed_url = self.url.format(host=self.server, code=self.event_code)
        self.complete_Service_File()
