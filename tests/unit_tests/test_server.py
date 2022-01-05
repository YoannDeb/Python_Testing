from server import loadClubs


class TestDbLoading:
    def test_loadClubs(self):
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
