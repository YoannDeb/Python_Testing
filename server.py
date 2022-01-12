import json
from flask import Flask,render_template,request,redirect,flash,url_for
from forms.forms import RegistrationForm


def loadClubs():
    with open('clubs.json') as c:
         listOfClubs = json.load(c)['clubs']
         return listOfClubs


def loadCompetitions():
    with open('competitions.json') as comps:
         listOfCompetitions = json.load(comps)['competitions']
         return listOfCompetitions


app = Flask(__name__)
app.secret_key = 'something_special'

competitions = loadCompetitions()
clubs = loadClubs()

@app.route('/')
def index():
    form = RegistrationForm(request.form, label="Email:")
    return render_template('index.html', form=form)

@app.route('/showSummary',methods=['POST'])
def showSummary():
    form = RegistrationForm(request.form, label="Email:")
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
    if foundClub and foundCompetition:
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
    if placesRequired > available_club_points:
        flash("Club doesn't have enough points to book this amount of places.")
    elif placesRequired + club[f"{competition['name']}_{competition['date']}_purchase_history"] > 12:
        flash("You can't book more than 12 places in a single competition.")
    else:
        competition['numberOfPlaces'] = int(competition['numberOfPlaces'])-placesRequired
        club[f"{competition['name']}_{competition['date']}_purchase_history"] += placesRequired
        flash('Great-booking complete!')
    return render_template('welcome.html', club=club, competitions=competitions)


# TODO: Add route for points display


@app.route('/logout')
def logout():
    return redirect(url_for('index'))
