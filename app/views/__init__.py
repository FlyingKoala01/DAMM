from flask import Blueprint, render_template, url_for, redirect, make_response, send_from_directory, request
from ..models import Bar

app = Blueprint('main', __name__)

@app.route('/')
def index():
    return redirect(url_for('.leaderboard'))

@app.route('/leaderboard', methods=['GET'])
def leaderboard():
    page = request.args.get('page', 1, type=int)
    per_page = 8
    bars_page = Bar.query.paginate(page, per_page, error_out=False)
    return render_template('pages/leaderboard.html.j2', bars_page=bars_page)


