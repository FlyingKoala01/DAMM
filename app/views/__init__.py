from flask import Blueprint, render_template, url_for, redirect, make_response, send_from_directory


app = Blueprint('main', __name__)

@app.route('/')
def index():
    return redirect(url_for('.leaderboard'))

@app.route('/leaderboard', methods=['GET'])
def leaderboard():
    return render_template('pages/leaderboard.html.j2')

@app.route('/serviceworker.js')
def service_worker():
    response = make_response(send_from_directory('static/js/','serviceworker.js'))
    response.headers['Content-Type'] = 'application/javascript'
    response.headers['Service-Worker-Allowed'] = '/'
    return response
