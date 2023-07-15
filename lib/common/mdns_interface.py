from .utilities import Run_Cmd
from ipaddress import IPv4Address

class MDNS_Record():

    def __init__(self, record_str):
        record_list = record_str.split(";")
        self.name = record_list[3]
        self.type = record_list[4]
        self.hostname = record_list[6]
        self.IP = IPv4Address(record_list[7])
        self.text = record_list[9]

class MDNS_Interface():

    def __init__(self, record_type):
        self.record_type = record_type
        self.records = []
        return
    
    def browse(self):
        output = Run_Cmd("avahi-browse -trpk {}".format(self.record_type))
        if output is not None:
            for record in output.split("\n"):
                if record.startswith("=;"):
                    if "IPv4" in record:
                        self.update_record(MDNS_Record(record))
        return
    
    def update_record(self, new_record: MDNS_Record):
        for index, record in enumerate(self.records):
            if new_record.hostname == record.hostname:
                self.records.pop(index)
                self.records.append(new_record)
                break
        else:
            self.records.append(new_record)

        