
from library.band import Band
from library.concert import Concert
from library.venue import Venue


def main():
    # Example Band, Venue, and Concert IDs
    band_id = 1
    venue_id = 1
    concert_id = 1

    band = Band(band_id)
    print(band.concerts())
    print(band.venues())
    print(band.all_introductions())
    print(band.most_performances())

    venue = Venue(venue_id)
    print(venue.concerts())
    print(venue.bands())
    print(venue.concert_on('2001-9-11'))
    print(venue.most_frequent_band())

    concert = Concert(concert_id)
    print(concert.band())
    print(concert.venue())
    print(concert.hometown_show())
    print(concert.introduction())

if __name__ == "__main__":
    main()