# p2app/engine/main.py
#
# ICS 33 Fall 2023
# Project 2: Learning to Fly
#
# An object that represents the engine of the application.
#
# This is the outermost layer of the part of the program that you'll need to build,
# which means that YOU WILL DEFINITELY NEED TO MAKE CHANGES TO THIS FILE.


import sqlite3
from p2app.events import *
from p2app.engine.continent import ContinentModule
from p2app.engine.country import CountryModule
from p2app.engine.region import RegionModule


class Engine:
    """An object that represents the application's engine, whose main role is to
    process events sent to it by the user interface, then generate events that are
    sent back to the user interface in response, allowing the user interface to be
    unaware of any details of how the engine is implemented.
    """

    def __init__(self):
        """Initializes the engine"""
        self.connection = None
        self.continent_connection = None
        self.country_connection = None
        self.region_connection = None

    def process_event(self, event):
        """A generator function that processes one event sent from the user interface,
        yielding zero or more events in response."""

        if isinstance(event, OpenDatabaseEvent):
            try:
                database_path = event.path()
                self.connection = sqlite3.connect(database_path)
                self.connection.execute("SELECT * FROM continent")
                self.connection.execute("SELECT * FROM country")
                self.connection.execute("SELECT * FROM region")
                self.connection.execute('PRAGMA foreign_keys = ON;')
                self.continent_connection = ContinentModule(self.connection)
                self.country_connection = CountryModule(self.connection)
                self.region_connection = RegionModule(self.connection)
                yield DatabaseOpenedEvent(database_path)

            except sqlite3.Error:
                yield DatabaseOpenFailedEvent('Invalid database file!')

        elif isinstance(event, CloseDatabaseEvent):
            if self.connection:
                self.connection.close()
            yield DatabaseClosedEvent()

        elif isinstance(event, QuitInitiatedEvent):
            yield EndApplicationEvent()

        elif isinstance(event, StartContinentSearchEvent):
            yield from self.continent_connection.start_continent_search(event)
            self.connection.commit()

        elif isinstance(event, LoadContinentEvent):
            yield from self.continent_connection.load_continent(event)
            self.connection.commit()

        elif isinstance(event, SaveNewContinentEvent):
            yield from self.continent_connection.save_new_continent(event)
            self.connection.commit()

        elif isinstance(event, SaveContinentEvent):
            yield from self.continent_connection.save_continent(event)
            self.connection.commit()

        elif isinstance(event, StartCountrySearchEvent):
            yield from self.country_connection.start_country_search(event)
            self.connection.commit()

        elif isinstance(event, LoadCountryEvent):
            yield from self.country_connection.load_country(event)
            self.connection.commit()

        elif isinstance(event, SaveNewCountryEvent):
            yield from self.country_connection.save_new_country(event)
            self.connection.commit()

        elif isinstance(event, SaveCountryEvent):
            yield from self.country_connection.save_country(event)
            self.connection.commit()

        elif isinstance(event, StartRegionSearchEvent):
            yield from self.region_connection.start_region_search(event)
            self.connection.commit()

        elif isinstance(event, LoadRegionEvent):
            yield from self.region_connection.load_region(event)
            self.connection.commit()

        elif isinstance(event, SaveNewRegionEvent):
            yield from self.region_connection.save_new_region(event)
            self.connection.commit()

        elif isinstance(event, SaveRegionEvent):
            yield from self.region_connection.save_region(event)
            self.connection.commit()