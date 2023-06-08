from flask import Blueprint, render_template, url_for, redirect, make_response, send_from_directory, request
from ..models import Bar
from sqlalchemy import desc, asc

app = Blueprint('main', __name__)

@app.route('/')
def index():
    return redirect(url_for('.leaderboard'))

@app.route('/leaderboard', methods=['GET'])
def leaderboard():
    page = request.args.get('page', 1, type=int)
    per_page = 8
    sort_by = request.args.get('sort_by', 'position', type=str)
    sort_order = request.args.get('sort_order', 'asc', type=str)
    
    column_mapping = {
        'position': Bar.position,
        'name': Bar.name,
        'grade': Bar.grade,
        'sales': Bar.total_sales,
        'progress': Bar.progress
    }

    if sort_order == 'desc':
        bars_page = Bar.query.order_by(desc(column_mapping[sort_by])).paginate(page, per_page, error_out=False)
    elif sort_order == 'asc':
        bars_page = Bar.query.order_by(asc(column_mapping[sort_by])).paginate(page, per_page, error_out=False)
    else:
        bars_page = Bar.query.order_by(sort_order(column_mapping[sort_by])).paginate(page, per_page, error_out=False)

    return render_template('pages/leaderboard.html.j2', bars_page=bars_page, sort_order=sort_order, sort_by=sort_by)