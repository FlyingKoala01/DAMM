from flask import Blueprint, render_template, url_for, redirect, make_response, send_from_directory
from ..models import Bar

app = Blueprint('main', __name__)

@app.route('/')
def index():
    return redirect(url_for('.leaderboard'))

@app.route('/leaderboard', methods=['GET'])
def leaderboard():

    bars = Bar.query.all()

    return render_template('pages/leaderboard.html.j2', bars = bars)

