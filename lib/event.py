import sqlite3
from datetime import datetime
from urllib.request import urlopen
import json
from pathlib import Path



class Event:
    def __init__(self, code, name, start, end, region):
        self.code = code
        self.name = name
        self.region = region
        self.start = datetime.fromtimestamp(start/1000+3600*6)
        self.end = datetime.fromtimestamp(end/1000+3600*6)
        self.event_info = {}
        self.load_JSON()
    
    def __str__(self):
        return "{}:{} in the {} Region".format(self.code, self.name,self.region)

    def load_JSON(self):
        url = "http://localhost/api/v2/events/"+self.code+"/full/"
        response = urlopen(url)
        data = json.loads(response.read())
        if not data:
            print("Response from URL was empty! {}".format(url))
            return False
        else:
            self.event_info = data
            return True
    
    


#my_event = load_JSON_From_URL(url)