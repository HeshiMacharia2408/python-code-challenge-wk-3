import sqlite3

class Venue:
    def __init__(self, venue_id):
        self.venue_id = venue_id

    def concerts(self):
        query = "SELECT * FROM concerts WHERE venue_id = ?"
        return self._execute_query(query, (self.venue_id,))

    def bands(self):
        query = """
        SELECT DISTINCT bands.* FROM bands
        JOIN concerts ON bands.id = concerts.band_id
        WHERE concerts.venue_id = ?
        """
        return self._execute_query(query, (self.venue_id,))

    def concert_on(self, date):
        query = "SELECT * FROM concerts WHERE venue_id = ? AND date = ? ORDER BY date LIMIT 1"
        return self._execute_query(query, (self.venue_id, date))

    def most_frequent_band(self):
        query = """
        SELECT bands.*, COUNT(concerts.id) as performance_count
        FROM bands
        JOIN concerts ON bands.id = concerts.band_id
        WHERE concerts.venue_id = ?
        GROUP BY bands.id
        ORDER BY performance_count DESC LIMIT 1
        """
        return self._execute_query(query, (self.venue_id,))

    def _execute_query(self, query, params):
        with sqlite3.connect('concerts.db') as conn:  # Adjust database path as needed
            cur = conn.cursor()
            cur.execute(query, params)
            return cur.fetchall()  # Fetch all results
