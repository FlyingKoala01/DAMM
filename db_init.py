# Database initialization, see README.md for more info.
from app import app, db
import os, utils

# # Remove the database file if it exists
# if os.path.exists('app/damm.db'):
#     os.remove('app/damm.db')

# # Create app tables
# with app.app_context():
#     db.create_all()

# # Connect to the database and populate them
# utils.script_excel_to_sql.main()
# print("Base de datos lista. Añade direcciones de establecimientos manualmente en otro terminal.")
# input("Una vez hecho, presione ENTER para cargar las valoraciones de Google.")
# utils.scrapper.monthly_review_all_months()

utils.rate.calc_rate_all_months()
utils.rate.cache_last_note()
