from .utilities import Run_Cmd
from ipaddress import IPv4Address

class MDNS_Record():

    def __init__(self, record_str):
        record_list = record_str.split(";")
        self.name = record_list[3]
        self.type = record_list[4]
        self.hostname = record_list[6]
        self.IP = IPv4Address(record_list[7])
        self.text = record_list[9].strip("\"")

class MDNS_Interface():

    def __init__(self, record_type):
        self.record_type = record_type
        self.records = []
        return
    
    def browse(self):
        self.records = []
        output = Run_Cmd("avahi-browse -trpk {}".format(self.record_type))
        if output is not None:
            for record in output.split("\n"):
                if record.startswith("=;"):
                    if "IPv4" in record:
                        self.records.append(MDNS_Record(record))
        return


        