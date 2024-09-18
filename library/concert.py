import sqlite3

class Concert:
    def __init__(self, concert_id):
        self.concert_id = concert_id

    def band(self):
        query = """
        SELECT bands.* FROM bands
        JOIN concerts ON bands.id = concerts.band_id
        WHERE concerts.id = ?
        """
        return self._execute_query(query, (self.concert_id,))

    def venue(self):
        query = """
        SELECT venues.* FROM venues
        JOIN concerts ON venues.id = concerts.venue_id
        WHERE concerts.id = ?
        """
        return self._execute_query(query, (self.concert_id,))

    def hometown_show(self):
        query = """
        SELECT bands.hometown, venues.city
        FROM bands
        JOIN concerts ON bands.id = concerts.band_id
        JOIN venues ON concerts.venue_id = venues.id
        WHERE concerts.id = ?
        """
        result = self._execute_query(query, (self.concert_id,))
        return result[0][0] == result[0][1]

    def introduction(self):
        query = """
        SELECT bands.name, bands.hometown, venues.city
        FROM bands
        JOIN concerts ON bands.id = concerts.band_id
        JOIN venues ON concerts.venue_id = venues.id
        WHERE concerts.id = ?
        """
        result = self._execute_query(query, (self.concert_id,))
        return f"Hello {result[0][2]}!!!!! We are {result[0][0]} and we're from {result[0][1]}!"

    def _execute_query(self, query, params):
        with sqlite3.connect('concerts.db') as conn:  # Adjust the database path as necessary
            cur = conn.cursor()
            cur.execute(query, params)
            return cur.fetchall()  # Fetch all results
