import unittest
from library.venue import Venue

class TestVenue(unittest.TestCase):
    def setUp(self):
        self.venue = Venue(1)

    def test_venue_concerts(self):
        concerts = self.venue.concerts()
        self.assertIsInstance(concerts, list)
        print("Venue Concerts:", concerts)

    def test_venue_bands(self):
        bands = self.venue.bands()
        self.assertIsInstance(bands, list)
        print("Bands at Venue:", bands)

    def test_concert_on(self):
        concert = self.venue.concert_on('2024-09-14')
        self.assertIsInstance(concert, list)
        print("Concert on Date:", concert)

    def test_most_frequent_band(self):
        most_frequent_band = self.venue.most_frequent_band()
        self.assertIsInstance(most_frequent_band, list)
        print("Most Frequent Band:", most_frequent_band)

if __name__ == "__main__":
    unittest.main()