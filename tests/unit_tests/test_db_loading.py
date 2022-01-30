from server import loadClubs, loadCompetitions


def test_loadClubs_should_return_clubs():
    """
    GIVEN the original json clubs' data file exists and is accessible
    WHEN loadClubs function is used to create clubs variable
    THEN clubs variable contains correct club data.
    """
    clubs = loadClubs()
    assert clubs[0:3] == [
        {
            "name": "Simply Lift",
            "email": "john@simplylift.co",
            "points": "13"
        },
        {
            "name": "Iron Temple",
            "email": "admin@irontemple.com",
            "points": "4"
        },
        {"name": "She Lifts",
         "email": "kate@shelifts.co.uk",
         "points": "12"
         }
    ]


def test_loadCompetitions_should_return_competitions():
    """
    GIVEN the original json competitions' data file exists and is accessible
    WHEN loadClubs function is used to create competitions variable
    THEN competitions variable contains correct competition data.
    """
    competitions = loadCompetitions()
    assert competitions[0:2] == [
        {
            "name": "Spring Festival",
            "date": "2029-03-27 10:00:00",
            "numberOfPlaces": "25"
        },
        {
            "name": "Fall Classic",
            "date": "2020-10-22 13:30:00",
            "numberOfPlaces": "13"
        }
    ]
