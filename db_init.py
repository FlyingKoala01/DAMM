# Database initialization, see README.md for more info.
from app import app, db
import os
import utils.script_excel_to_sql
import utils.rate

# Remove the database file if it exists
if os.path.exists('app/damm.db'):
    os.remove('app/damm.db')

# Create app tables
with app.app_context():
    db.create_all()

# Connect to the database and populate them
utils.script_excel_to_sql.main()
#utils.rate.rate()
