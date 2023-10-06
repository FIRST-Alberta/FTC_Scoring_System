
class Display:
    def __init__(self, hostname, role, ip_address, event_code):
        self.hostname = hostname
        self.role = role
        self.address = ip_address
        self.event_code = event_code
        self.server = ""
        self.url = ""
        self.completed_file = ""
        self.completed_url = ""
        self.service_file = "".join(["<service-group>\n",
                                     "  <name>{role}</name>\n",
                                     "  <service>\n",
                                     "    <type>_display._tcp</type>\n",
                                     "    <port>8080</port>\n",
                                     "    <txt-record>{event}</txt-record>\n",
                                     "  </service>\n",
                                     "</service-group>"])
    
    def __str__(self):
        return "{}  (Role: {})  (Event: {})".format(self.hostname, self.role, self.event_code)

    def Apply_Config(self, config: dict):
        pass

    def complete_Service_File(self):
        self.completed_file = self.service_file.format(role=self.role, event=self.event_code)

    def apply_server_name(self, name):
        if "192.168.100" in name:
            self.server = name
        elif ".local" in name:
            self.server = name
        else:
            self.server = name + ".local"

        


