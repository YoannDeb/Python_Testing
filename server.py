import json
from flask import Flask,render_template,request,redirect,flash,url_for
from forms.forms import RegistrationForm
import datetime


def loadClubs():
    with open('clubs.json') as c:
         listOfClubs = json.load(c)['clubs']
         return listOfClubs


def loadCompetitions():
    with open('competitions.json') as comps:
         listOfCompetitions = json.load(comps)['competitions']
         return listOfCompetitions


def register_club_points_in_clubs(modified_club):
    list_position = 0
    for club in clubs:
        if club['name'] == modified_club['name']:
            club_position = list_position
            break
    clubs[club_position] = modified_club


def register_competition_in_competitions(modified_competition):
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
    form = RegistrationForm(request.form)
    return render_template('index.html', form=form)

@app.route('/showSummary',methods=['POST'])
def showSummary():
    form = RegistrationForm(request.form)
    if form.validate():
        email = form.email.data
        if email not in [club['email'] for club in clubs]:
            return render_template('index.html', form=form, message="You are not secretary of a club. Please input a secretary email.", style="color:red")
        club = [club for club in clubs if club['email'] == email][0]
        return render_template('welcome.html',club=club,competitions=competitions, form=form)
    return redirect(url_for('index'))


@app.route('/book/<competition>/<club>')
def book(competition,club):
    foundClub = [c for c in clubs if c['name'] == club][0]
    foundCompetition = [c for c in competitions if c['name'] == competition][0]
    competition_date = datetime.datetime(year=int(foundCompetition['date'][:4]),
                                         month=int(foundCompetition['date'][5:7]),
                                         day=int(foundCompetition['date'][8:10]),
                                         hour=int(foundCompetition['date'][11:13]),
                                         minute=int(foundCompetition['date'][14:16]),
                                         second=int(foundCompetition['date'][17:18]))
    if foundClub and foundCompetition:
        if competition_date < datetime.datetime.now():
            flash("You can't book a place for past competitions.")
            return render_template('welcome.html', club=club, competitions=competitions)
        return render_template('booking.html',club=foundClub,competition=foundCompetition)
    else:
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/purchasePlaces',methods=['POST'])
def purchasePlaces():
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
    elif placesRequired > available_club_points:
        flash("Club doesn't have enough points to book this amount of places.")
    elif placesRequired + club[f"{competition['name']}_{competition['date']}_purchase_history"] > 12:
        flash("You can't book more than 12 places in a single competition.")
    else:
        competition['numberOfPlaces'] = str(int(competition['numberOfPlaces'])-placesRequired)
        club['points'] = str(int(club['points']) - placesRequired)
        club[f"{competition['name']}_{competition['date']}_purchase_history"] += placesRequired
        register_competition_in_competitions(competition)
        register_club_points_in_clubs(club)
        flash('Great-booking complete!')
    return render_template('welcome.html', club=club, competitions=competitions)


# TODO: Add route for points display


@app.route('/logout')
def logout():
    return redirect(url_for('index'))
