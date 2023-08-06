from .common.mdns_interface import MDNS_Interface
from tabulate import tabulate
from .display import Display
from .common.utilities import Run_Cmd

class Display_Manager():

    def __init__(self):
        self.mdns = MDNS_Interface("_display._tcp")
        self.update_Display_List()
        self.server_hostname = Run_Cmd("hostname") + ".local"

    @property
    def displays(self):
        return self.mdns.records

    def update_Display_List(self):
        self.mdns.browse()

    def print_Displays(self):
        table = [["Hostname", "Role", "IP Address", "Expires"]]
        for record in self.displays:
            table.append([record.hostname, record.name, record.IP, record.text])
        print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
    
    def config_Display(self, hostname, role, event):
        display = Display(hostname)
        display.Build_Config(self.server_hostname, event, role)