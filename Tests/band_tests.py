from library.band import Band

def test_band_concerts():
    band = Band(1)
    concerts = band.concerts()
    print("Band Concerts:", concerts)

def test_band_venues():
    band = Band(1)
    venues = band.venues()
    print("Band Venues:", venues)

def test_play_in_venue():
    band = Band(1)
    band.play_in_venue('Royal Albert Hall', '2024-09-17')
    print("New concert added for Band 1")

def test_all_introductions():
    band = Band(1)
    introductions = band.all_introductions()
    print("All Introductions:")
    for intro in introductions:
        print(intro)

def test_most_performances():
    most_performing_band = Band.most_performances()
    print("Most Performing Band:", most_performing_band)

if __name__ == "__main__":
    test_band_concerts()
    test_band_venues()
    test_play_in_venue()
    test_all_introductions()
    test_most_performances()
