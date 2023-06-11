# Database initialization, see README.md for more info.
from app import app, db, bcrypt
import sqlite3, os
import script_excel_to_sql
import rate


DEFAULT_PWD = os.environ['DAMM_DEFAULT_PASSWORD'] if 'DAMM_DEFAULT_PASSWORD' in os.environ else '1234ABc$'
ENCRYPTED_DEFAULT_PWD = bcrypt.generate_password_hash(DEFAULT_PWD)

# Remove the database file if it exists
if os.path.exists('app/damm.db'):
    os.remove('app/damm.db')

# Create app tables
with app.app_context():
    db.create_all()

# Connect to the database and populate them
script_excel_to_sql.main()
rate.rate()

