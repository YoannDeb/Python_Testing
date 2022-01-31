import json
from flask import Flask, render_template, request, redirect, flash, url_for
from forms.forms import RegistrationForm
import datetime

POINTS_PER_PLACE = 3

def loadClubs():
    """
    Loads clubs' data from json file.
    Data is for testing purpose.
    As it's an MVP, it avoids use of a database.
    Data is not saved in json, so it's reset with server restart.
    :return: ListOfClubs: The list of clubs from json file.
    """
    with open('clubs.json') as c:
         listOfClubs = json.load(c)['clubs']
         return listOfClubs


def loadCompetitions():
    """
    Loads competitions' data from json file.
    Data is for testing purpose.
    As it's an MVP, it avoids use of a database.
    Data is not saved in json, so it's reset with server restart.
    :return: ListOfClubs: The list of clubs from json file.
    """
    with open('competitions.json') as comps:
         listOfCompetitions = json.load(comps)['competitions']
         return listOfCompetitions


def register_club_points_in_clubs(modified_club):
    """
    Registers club modified data in clubs global variable
    :param modified_club: clubs data that is to be registered.
    """
    list_position = 0
    for club in clubs:
        if club['name'] == modified_club['name']:
            club_position = list_position
            break
    clubs[club_position] = modified_club


def register_competition_in_competitions(modified_competition):
    """
    Registers competition modified data in clubs global variable
    :param modified_competition: clubs data that is to be registered.
    """
    list_position = 0
    for competition in competitions:
        if competition['name'] == modified_competition['name']:
            competition_position = list_position
            break
    competitions[competition_position] = modified_competition


app = Flask(__name__)
app.secret_key = 'something_special'

competitions = loadCompetitions()
clubs = loadClubs()

@app.route('/')
def index():
    """
    Route for index page.
    Using a form to get user's email for login.
    Mail must be valid and be part of the clubs' emails. That last point is verified in showSummary.
    :return: A render of the index.html template.
    """
    form = RegistrationForm(request.form)
    return render_template('index.html', form=form)

@app.route('/showSummary', methods=['POST'])
def showSummary():
    """
    Route for showSummary page, which shows email of logged user, all competitions etc.
    First checks if email is part of clubs' emails.
    If not, it redirects to index with appropriate error message.
    If so, the club is selected to be sent to the template.
    :return: A redirection to index if form is not valid. Else a render of the appropriate template.
    """
    form = RegistrationForm(request.form)
    if form.validate():
        email = form.email.data
        if email not in [club['email'] for club in clubs]:
            return render_template('index.html', form=form, message="You are not secretary of a club. Please input a secretary email.", style="color:red")
        club = [club for club in clubs if club['email'] == email][0]
        return render_template('welcome.html', club=club, competitions=competitions, form=form)
    return redirect(url_for('index'))


@app.route('/book/<competition>/<club>')
def book(competition, club):
    """
    Route for booking page, which let the user enter the number of places he wants.
    Access is denied for past competitions.
    :param competition: The competition the user is booking for.
    :param club: The user's club.
    :return: A render of the appropriate template.
    """

    found_club_list = [c for c in clubs if c['name'] == club]
    if found_club_list:
        foundClub = found_club_list[0]
    else:
        foundClub = None
    found_competition_list = [c for c in competitions if c['name'] == competition]
    if found_competition_list:
        foundCompetition = found_competition_list[0]
    else:
        foundCompetition = None

    if foundClub and foundCompetition:
        competition_date = datetime.datetime(year=int(foundCompetition['date'][:4]),
                                             month=int(foundCompetition['date'][5:7]),
                                             day=int(foundCompetition['date'][8:10]),
                                             hour=int(foundCompetition['date'][11:13]),
                                             minute=int(foundCompetition['date'][14:16]),
                                             second=int(foundCompetition['date'][17:18]))
        if competition_date < datetime.datetime.now():
            flash("You can't book a place for past competitions.")
            return render_template('welcome.html', club=foundClub, competitions=competitions)
        return render_template('booking.html', club=foundClub, competition=foundCompetition)
    elif foundClub:
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=foundClub, competitions=competitions)
    else:
        form = RegistrationForm(request.form)
        return render_template('index.html', form=form, message="Something went wrong, please enter your mail again.", style="color:red")


@app.route('/purchasePlaces', methods=['POST'])
def purchasePlaces():
    """
    Route for purchasePlaces.
    Checks if the place reservation is possible.
    Constraints are:
    - places number greater than 0
    - sufficient clubs' points count
    - 12 places maximum per club and competition
    If purchase is valid, performs modification of the data, and saving.
    A message is flashed in the template to inform user what happened.
    note: Using the POINTS_PER_PLACE constant, which is currently 3.
    :return: A render of the welcome.html template.
    """
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    try:
        club[f"{competition['name']}_{competition['date']}_purchase_history"]
    except KeyError:
        club[f"{competition['name']}_{competition['date']}_purchase_history"] = 0

    placesRequired = int(request.form['places'])
    available_club_points = int(club['points'])
    if placesRequired <= 0:
        flash("The number of places must be greater than 0 to be valid.")
    elif placesRequired > (available_club_points/POINTS_PER_PLACE):
        flash("Club doesn't have enough points to book this amount of places.")
    elif placesRequired + club[f"{competition['name']}_{competition['date']}_purchase_history"] > 12:
        flash("You can't book more than 12 places in a single competition.")
    else:
        competition['numberOfPlaces'] = str(int(competition['numberOfPlaces'])-placesRequired)
        club['points'] = str(int(club['points']) - (placesRequired * POINTS_PER_PLACE))
        club[f"{competition['name']}_{competition['date']}_purchase_history"] += placesRequired
        register_competition_in_competitions(competition)
        register_club_points_in_clubs(club)
        flash('Great-booking complete!')
    return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/pointsDisplay')
def PointsDisplay():
    """
    Route for pointsDisplay template, which shows a table of all clubs and the points they have.
    This page is public, no needs to be logged in to consult it.
    :return: A render of the pointsdisplay.html page.
    """
    return render_template('pointsdisplay.html', clubs=clubs)


@app.route('/logout')
def logout():
    """
    Route for logout.
    the redirection breaks the authentification as it is now.
    :return: A redirection to index page
    """
    return redirect(url_for('index'))
