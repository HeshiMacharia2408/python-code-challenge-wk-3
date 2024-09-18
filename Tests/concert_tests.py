import unittest
from library.concert import Concert

class TestConcert(unittest.TestCase):
    def setUp(self):
        self.concert = Concert(1)

    def test_concert_band(self):
        band = self.concert.band()
        self.assertIsNotNone(band)
        print("Concert Band:", band)

    def test_concert_venue(self):
        venue = self.concert.venue()
        self.assertIsNotNone(venue)
        print("Concert Venue:", venue)

    def test_hometown_show(self):
        is_hometown = self.concert.hometown_show()
        self.assertIsInstance(is_hometown, bool)
        print("Is Hometown Show:", is_hometown)

    def test_introduction(self):
        introduction = self.concert.introduction()
        self.assertIsInstance(introduction, str)
        print("Concert Introduction:", introduction)

if __name__ == "__main__":
    unittest.main()