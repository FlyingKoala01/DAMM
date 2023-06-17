from flask import Blueprint, render_template, url_for, redirect, make_response, send_from_directory, request
from ..models import Establecimiento
from sqlalchemy import desc, asc

app = Blueprint('main', __name__)

@app.route('/')
def index():
    return redirect(url_for('.leaderboard'))

@app.route('/leaderboard', methods=['GET'])
def leaderboard():
    page = request.args.get('page', 1, type=int)
    per_page = 10
    sort_order = request.args.get('sort_order', 'desc', type=str)
    sort_function = desc if sort_order=='desc' else asc
    filter_name = request.args.get('q', '', type=str)

    bars_page = Establecimiento.query.filter(Establecimiento.nombre.contains(filter_name)).order_by(sort_function(Establecimiento.nota)).paginate(page, per_page, error_out=False)
    return render_template('pages/leaderboard.html.j2', bars_page=bars_page, sort_order=sort_order, filter_name=filter_name)
