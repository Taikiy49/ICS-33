import sqlite3
from p2app.events import *


class RegionModule:
    def __init__(self, connection: sqlite3.Connection):
        """Initializes a RegionModule with a database connection."""
        self.connection = connection

    def start_region_search(self, event: StartRegionSearchEvent):
        """Starts a search for regions based on provided criteria."""
        if self.connection:
            region_code = event.region_code()
            local_code = event.local_code()
            name = event.name()
            cursor = self.connection.cursor()

            if region_code and local_code and name:
                cursor.execute("SELECT region_id, continent_id, country_id, wikipedia_link, "
                               "keywords FROM region WHERE region_code = ? AND local_code = ? AND "
                               "name = ?", (region_code, local_code, name))
                region_infos = cursor.fetchall()
                if region_infos:
                    for info in region_infos:
                        yield RegionSearchResultEvent(Region(info[0], region_code, local_code, name, info[1],
                                                             info[2], info[3], info[4]))
            elif region_code and local_code:
                cursor.execute("SELECT region_id, name, continent_id, country_id, wikipedia_link, keywords "
                               "FROM region WHERE region_code = ? AND local_code = ?", (region_code, local_code))
                region_infos = cursor.fetchall()
                if region_infos:
                    for info in region_infos:
                        yield RegionSearchResultEvent(
                            Region(info[0], region_code, local_code, info[1], info[2], info[3],
                                   info[4], info[5]))

            elif local_code and name:
                cursor.execute("SELECT region_id, region_code, continent_id, country_id, wikipedia_link, keywords "
                               "FROM region WHERE local_code = ? AND name = ?", (local_code, name))
                region_infos = cursor.fetchall()
                if region_infos:
                    for info in region_infos:
                        yield RegionSearchResultEvent(Region(info[0], info[1], local_code, name, info[2], info[3],
                                                             info[4], info[5]))

            elif region_code and name:
                cursor.execute("SELECT region_id, local_code, continent_id, country_id, wikipedia_link, keywords "
                               "FROM region WHERE region_code = ? AND name = ?", (region_code, name))
                region_infos = cursor.fetchall()
                if region_infos:
                    for info in region_infos:
                        yield RegionSearchResultEvent(Region(info[0], region_code, info[1], name, info[2],
                                                             info[3], info[4], info[5]))

            elif region_code:
                cursor.execute("SELECT region_id, local_code, name, continent_id, country_id, wikipedia_link, "
                               "keywords FROM region WHERE region_code = ?", (region_code,))
                region_infos = cursor.fetchall()
                if region_infos:
                    for info in region_infos:
                        yield RegionSearchResultEvent(Region(info[0], region_code, info[1], info[2], info[3],
                                                             info[4], info[5], info[6]))
            elif local_code:
                cursor.execute("SELECT region_id, region_code, name, continent_id, country_id, wikipedia_link, "
                               "keywords FROM region WHERE local_code = ?", (local_code,))
                region_infos = cursor.fetchall()
                if region_infos:
                    for info in region_infos:
                        yield RegionSearchResultEvent(Region(info[0], info[1], local_code, info[2], info[3],
                                                             info[4], info[5], info[6]))

            elif name:
                cursor.execute("SELECT region_id, region_code, local_code, continent_id, country_id, "
                               "wikipedia_link, keywords FROM region WHERE name = ?", (name,))
                region_infos = cursor.fetchall()
                if region_infos:
                    for info in region_infos:
                        yield RegionSearchResultEvent(Region(info[0], info[1], info[2], name, info[3], info[4],
                                                             info[5], info[6]))
            cursor.close()

    def load_region(self, event: LoadRegionEvent):
        """Loads region information based on its ID."""
        region_id = event.region_id()
        cursor = self.connection.cursor()
        cursor.execute("SELECT region_code, local_code, name, continent_id, country_id, wikipedia_link, "
                       "keywords FROM region WHERE region_id = ?", (region_id,))
        region_infos = cursor.fetchall()
        cursor.close()
        if region_infos:
            for info in region_infos:
                yield RegionLoadedEvent(Region(region_id, info[0], info[1], info[2],
                                               info[3], info[4], info[5], info[6]))
        else:
            yield ErrorEvent("Loading a region failed.")

    def save_new_region(self, event: SaveNewRegionEvent):
        """Saves a new region to the database."""
        try:
            region = event.region()
            cursor = self.connection.cursor()

            none_list = []

            if region.region_code is None:
                none_list.append("")
            else:
                none_list.append(region.region_code)

            if region.local_code is None:
                none_list.append("")
            else:
                none_list.append(region.local_code)

            if region.name is None:
                none_list.append("")
            else:
                none_list.append(region.name)

            if region.continent_id is None:
                none_list.append("")
            else:
                none_list.append(region.continent_id)

            if region.country_id is None:
                none_list.append("")
            else:
                none_list.append(region.country_id)

            cursor.execute("INSERT INTO region (region_code, local_code, name, continent_id, country_id,"
                           "wikipedia_link, keywords) VALUES (?, ?, ?, ?, ?, ?, ?)",
                           (none_list[0], none_list[1], none_list[2], none_list[3],
                            none_list[4], region.wikipedia_link, region.keywords))
            cursor.close()

            yield RegionSavedEvent(region)

        except sqlite3.IntegrityError as e:
            if 'UNIQUE constraint failed' in str(e):
                yield SaveRegionFailedEvent("Please use a unique region code.")
            elif 'NOT NULL constraint failed' in str(e):
                yield SaveRegionFailedEvent("All inputs besides its wikipedia link and keywords cannot be empty.")
            elif 'FOREIGN KEY constraint failed' in str(e):
                yield SaveRegionFailedEvent("Continent id or country id does not exist in database.")

    def save_region(self, event: SaveRegionEvent):
        """Updates an existing region's information in the database."""
        try:
            region = event.region()
            cursor = self.connection.cursor()
            none_list = []

            if region.region_code is None:
                none_list.append("")
            else:
                none_list.append(region.region_code)

            if region.local_code is None:
                none_list.append("")
            else:
                none_list.append(region.local_code)

            if region.name is None:
                none_list.append("")
            else:
                none_list.append(region.name)

            if region.continent_id is None:
                none_list.append("")
            else:
                none_list.append(region.continent_id)

            if region.country_id is None:
                none_list.append("")
            else:
                none_list.append(region.country_id)

            cursor.execute("UPDATE region SET region_code = ?, local_code = ?, name = ?, continent_id = ?, "
                           "country_id = ?, wikipedia_link = ?, keywords = ? WHERE region_id = ?",
                           (none_list[0], none_list[1], none_list[2], none_list[3], none_list[4],
                            region.wikipedia_link, region.keywords, region.region_id))
            cursor.close()

            yield RegionSavedEvent(region)

        except sqlite3.IntegrityError as e:
            if 'UNIQUE constraint failed' in str(e):
                yield SaveRegionFailedEvent("Please use a unique region code.")
            elif 'NOT NULL constraint failed' in str(e):
                yield SaveRegionFailedEvent("All inputs besides its wikipedia link and keywords cannot be empty.")
            elif 'FOREIGN KEY constraint failed' in str(e):
                yield SaveRegionFailedEvent(
                    "Continent id or country id does not exist in the database.")

