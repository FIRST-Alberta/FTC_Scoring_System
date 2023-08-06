import sqlite3
from tabulate import tabulate
from .event import Event
from pathlib import Path

__SCOREKEEPER_PATH__ = Path("/usr/local/src/scorekeeper/")

class Event_Manager():

    def __init__(self) -> None:
        
        self.connection = sqlite3.connect(str(__SCOREKEEPER_PATH__ + "db/server.db"))
        self.cursor = self.connection.cursor()
        self.cursor.execute("SELECT * FROM Events")
        self.events = {}
        self.update_Events_Table()

    def update_Events_Table(self):
        events_table = self.cursor.fetchall()
        for entry in events_table:
            self.events[entry[0]] = Event(entry[0], entry[1], entry[6], entry[7], entry[8])

    def print_Events(self):
        table = [["Code", "Name", "Starts", "Ends"]]
        for entry in self.events.values():
            table.append([entry.code, entry.name, entry.start, entry.end])
        print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))