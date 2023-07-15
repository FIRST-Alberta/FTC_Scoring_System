from .common.mdns_interface import MDNS_Interface
from tabulate import tabulate

class Display_Manager():

    def __init__(self):
        self.mdns = MDNS_Interface("_display._tcp")
        self.update_Display_List()

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

    def hostname_Valid(self, hostname:str)->bool:
        for record in self.displays:
            if hostname == record.hostname:
                print("{} is a valid hostname.".format(hostname))
                return True
        else:
            print("{} is not a valid hostname.".format(hostname))
            return False

    def get_Hostname(self)-> str:
        hostname = input("Please enter a hostname:")
        while not self.hostname_Valid(hostname):
            hostname = input("Please enter a hostname:")
        return hostname