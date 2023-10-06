from .common.mdns_interface import MDNS_Interface
from .display import Display
from .common.utilities import Run_Cmd
from .audience_display import Audience_Display
from .field_display import Field_Display
from .inspection_display import Inspection_Display
from .pit_display import Pit_Display
from .sponsor_display import Sponsor_Display
 

class Display_Manager():

    def __init__(self):
        self.mdns = MDNS_Interface("_display._tcp")
        self.displays = []
        self.update_Display_List()
        self.server_hostname = Run_Cmd("hostname") + ".local"

    def update_Display_List(self):
        self.mdns.browse()
        self.displays = []
        for record in self.mdns.records:
            if "audience" in record.name:
                self.displays.append(Audience_Display(record.hostname, record.name, record.IP, record.text))
            elif "field" in record.name:
                self.displays.append(Field_Display(record.hostname, record.name, record.IP, record.text))
            elif "inspection" in record.name:
                self.displays.append(Inspection_Display(record.hostname, record.name, record.IP, record.text))
            elif "pit" in record.name:
                self.displays.append(Pit_Display(record.hostname, record.name, record.IP, record.text))
            elif "sponsor" in record.name:
                self.displays.append(Sponsor_Display(record.hostname, record.name, record.IP, record.text))

    def Change_Display_Role(self, display: Display, new_role: str=""):
        if display in self.displays:
            if "audience" in new_role:
                new_display = Audience_Display(display.hostname, new_role, display.address, display.event_code)
            elif "field" in new_role:
                new_display = Field_Display(display.hostname, new_role, display.address, display.event_code)
            elif "inspection" in new_role:
                new_display = Inspection_Display(display.hostname, new_role, display.address, display.event_code)
            elif "pit" in new_role:
                new_display = Pit_Display(display.hostname, new_role, display.address, display.event_code)
            elif "sponsor" in new_role:
                new_display = Sponsor_Display(display.hostname, new_role, display.address, display.event_code)
            else:
                return display
            self.displays.remove(display)
            self.displays.append(new_display)
            return new_display
        else:
            print("Invalid Display Object")
        