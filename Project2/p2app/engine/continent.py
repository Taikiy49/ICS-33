import sqlite3
from p2app.events import *


class ContinentModule:
    def __init__(self, connection: sqlite3.Connection):
        """Initializes a ContinentModule with a database connection."""
        self.connection = connection

    def start_continent_search(self, event: StartContinentSearchEvent):
        """Starts a search for continent based on the provided criteria."""
        if self.connection:
            continent_code = event.continent_code()
            name = event.name()
            cursor = self.connection.cursor()
            if continent_code and name:
                cursor.execute("SELECT continent_id FROM continent WHERE continent_code = ? and "
                               "name = ?", (continent_code, name))
                continent_infos = cursor.fetchall()
                if continent_infos:
                    for info in continent_infos:
                        yield ContinentSearchResultEvent(Continent(info[0], continent_code, name))

            elif continent_code:
                cursor.execute("SELECT continent_id, name FROM continent WHERE continent_code = ?", (continent_code, ))
                continent_infos = cursor.fetchall()
                if continent_infos:
                    for info in continent_infos:
                        yield ContinentSearchResultEvent(Continent(info[0], continent_code, info[1]))

            elif name:
                cursor.execute("SELECT continent_id, continent_code FROM continent WHERE name = ?", (name, ))
                continent_infos = cursor.fetchall()
                if continent_infos:
                    for info in continent_infos:
                        yield ContinentSearchResultEvent(Continent(info[0], info[1], name))
            cursor.close()

    def load_continent(self, event: LoadContinentEvent):
        """Loads continent information based on its continent id"""
        continent_id = event.continent_id()
        cursor = self.connection.cursor()
        cursor.execute("SELECT continent_code, name FROM continent WHERE continent_id = ?", (continent_id,))
        continent_info = cursor.fetchone()
        if continent_info:
            yield ContinentLoadedEvent(Continent(continent_id, continent_info[0], continent_info[1]))
        else:
            yield ErrorEvent("Loading a continent failed.")

    def save_new_continent(self, event: SaveNewContinentEvent):
        """Saves a new continent to the database."""
        try:
            continent = event.continent()
            cursor = self.connection.cursor()
            cursor.execute("INSERT INTO continent (continent_code, name)"
                           "VALUES (?, ?)", (continent.continent_code, continent.name))
            cursor.close()
            yield ContinentSavedEvent(continent)

        except sqlite3.IntegrityError:
            yield SaveContinentFailedEvent("Please enter a unique continent code.")

    def save_continent(self, event: SaveContinentEvent):
        """Updates an existing continent's information in the database."""
        try:
            continent = event.continent()
            cursor = self.connection.cursor()
            cursor.execute("UPDATE continent SET continent_code = ?, name = ? WHERE continent_id = ?",
                           (continent.continent_code, continent.name, continent.continent_id))
            cursor.close()
            yield ContinentSavedEvent(Continent(continent.continent_id,
                                                continent.continent_code, continent.name))

        except sqlite3.IntegrityError:
            yield SaveContinentFailedEvent("Please enter a unique continent code.")
