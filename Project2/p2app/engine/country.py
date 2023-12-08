import sqlite3
from p2app.events import *


class CountryModule:
    def __init__(self, connection: sqlite3.Connection):
        """Initializes a CountryModule with a database connection."""
        self.connection = connection

    def start_country_search(self, event: StartCountrySearchEvent):
        """Starts a search for countries based on the provided criteria."""
        if self.connection:
            country_code = event.country_code()
            country_name = event.name()
            cursor = self.connection.cursor()
            if country_code and country_name:
                cursor.execute("SELECT country_id, continent_id, wikipedia_link, keywords FROM country WHERE "
                               "country_code = ? AND name = ?", (country_code, country_name))
                country_infos = cursor.fetchall()
                if country_infos:
                    for info in country_infos:
                        yield CountrySearchResultEvent(Country(info[0], country_code, country_name, info[1],
                                                               info[2], info[3]))
            elif country_code:
                cursor.execute("SELECT country_id, name, continent_id, wikipedia_link, keywords FROM country "
                               "WHERE country_code = ?", (country_code,))
                country_infos = cursor.fetchall()
                if country_infos:
                    for info in country_infos:
                        yield CountrySearchResultEvent(Country(info[0], country_code, info[1], info[2],
                                                               info[3], info[4]))
            elif country_name:
                cursor.execute("SELECT country_id, country_code, continent_id, wikipedia_link, keywords FROM "
                               "country WHERE name = ?", (country_name,))
                country_infos = cursor.fetchall()
                if country_infos:
                    for info in country_infos:
                        yield CountrySearchResultEvent(Country(info[0], info[1], country_name, info[2],
                                                               info[3], info[4]))
            cursor.close()

    def load_country(self, event: LoadCountryEvent):
        """Loads country information based on its ID."""
        country_id = event.country_id()
        cursor = self.connection.cursor()


        cursor.execute("SELECT country_code, name, continent_id, wikipedia_link, keywords FROM country "
                       "WHERE country_id = ?", (country_id,))
        country_info = cursor.fetchone()

        if country_info:
            yield CountryLoadedEvent(Country(country_id, country_info[0], country_info[1], country_info[2],
                                             country_info[3], country_info[4]))
        else:
            yield ErrorEvent("Loading a country failed.")

        cursor.close()

    def save_new_country(self, event: SaveNewCountryEvent):
        """Saves a new country to the database."""
        try:
            country = event.country()
            cursor = self.connection.cursor()
            none_list = []

            if country.country_code is None:
                none_list.append("")
            else:
                none_list.append(country.country_code)

            if country.name is None:
                none_list.append("")
            else:
                none_list.append(country.name)

            if country.continent_id is None:
                none_list.append("")
            else:
                none_list.append(country.continent_id)

            if country.wikipedia_link is None:
                none_list.append("")
            else:
                none_list.append(country.wikipedia_link)

            cursor.execute("INSERT INTO country (country_code, name, continent_id, wikipedia_link, "
                           "keywords) VALUES (?, ?, ?, ?, ?)", (none_list[0], none_list[1],
                                                                none_list[2], none_list[3],
                                                                country.keywords))
            cursor.close()

            yield CountrySavedEvent(country)

        except sqlite3.IntegrityError as e:
            if 'NOT NULL constraint failed' in str(e):
                yield SaveCountryFailedEvent("All inputs besides its keywords cannot be empty.")
            elif 'UNIQUE constraint failed' in str(e):
                yield SaveCountryFailedEvent("Please use a unique country code.")
            elif 'FOREIGN KEY constraint failed' in str(e):
                yield SaveCountryFailedEvent("Continent id does not exist in database. "
                                             "Please choose an existing continent id.")

    def save_country(self, event: SaveCountryEvent):
        """Updates an existing country's information in the database."""
        try:
            country = event.country()
            cursor = self.connection.cursor()
            none_list = []

            if country.country_code is None:
                none_list.append("")
            else:
                none_list.append(country.country_code)

            if country.name is None:
                none_list.append("")
            else:
                none_list.append(country.name)

            if country.continent_id is None:
                none_list.append("")
            else:
                none_list.append(country.continent_id)

            if country.wikipedia_link is None:
                none_list.append("")
            else:
                none_list.append(country.wikipedia_link)

            cursor.execute(
                "UPDATE country SET country_code=?, name=?, continent_id=?, wikipedia_link=?, keywords=? "
                "WHERE country_id=?",
                (none_list[0], none_list[1], none_list[2], none_list[3],
                 country.keywords, country.country_id))

            cursor.close()

            yield CountrySavedEvent(country)

        except sqlite3.IntegrityError as e:
            if 'NOT NULL constraint failed' in str(e):
                yield SaveCountryFailedEvent("All inputs besides its keywords cannot be empty.")
            elif 'UNIQUE constraint failed' in str(e):
                yield SaveCountryFailedEvent("Please use a unique country code.")
            elif 'FOREIGN KEY constraint failed' in str(e):
                yield SaveCountryFailedEvent("Continent id does not exist in database. "
                                             "Please choose an existing continent id.")
