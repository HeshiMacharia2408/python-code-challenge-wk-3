import sqlite3

class Band:
    def __init__(self, band_id):
        self.band_id = band_id

    def concerts(self):
        query = "SELECT * FROM concerts WHERE band_id = ?"
        return self._execute_query(query, (self.band_id,))

    def venues(self):
        query = """
        SELECT DISTINCT venues.* FROM venues
        JOIN concerts ON venues.id = concerts.venue_id
        WHERE concerts.band_id = ?
        """
        return self._execute_query(query, (self.band_id,))

    def play_in_venue(self, venue_title, date):
        query = """
        INSERT INTO concerts (band_id, venue_id, date)
        SELECT ?, venues.id, ?
        FROM venues WHERE venues.title = ?
        """
        return self._execute_query(query, (self.band_id, date, venue_title))

    def all_introductions(self):
        query = """
        SELECT venues.city, bands.name, bands.hometown
        FROM concerts
        JOIN venues ON concerts.venue_id = venues.id
        JOIN bands ON concerts.band_id = bands.id
        WHERE concerts.band_id = ?
        """
        results = self._execute_query(query, (self.band_id,))
        introductions = [f"Hello {r[0]}!!!!! We are {r[1]} and we're from {r[2]}!" for r in results]
        return introductions

    @staticmethod
    def most_performances():
        query = """
        SELECT bands.*, COUNT(concerts.id) as performance_count
        FROM bands
        JOIN concerts ON bands.id = concerts.band_id
        GROUP BY bands.id
        ORDER BY performance_count DESC LIMIT 1
        """
        return Band._execute_query_static(query, ())

    def _execute_query(self, query, params):
        with sqlite3.connect('concerts.db') as conn:  # Adjust the path to your database if needed
            cur = conn.cursor()
            cur.execute(query, params)
            return cur.fetchall()

    @staticmethod
    def _execute_query_static(query, params):
        with sqlite3.connect('concerts.db') as conn:
            cur = conn.cursor()
            cur.execute(query, params)
            return cur.fetchall()
