"""
Computes the grade of each local according to data stored in the database. 
"""

import sqlite3
from weightings import weightings
from social_net import social_net
from math import log

DB_PATH='damm.bd'
months=["Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Sep","Oct","Nov","Dec"]

SOCIAL_NETWORKS_WEIGHT=0.5
DATABASE_SALES_WEIGHT=0.5


def weightLocal(local,month=None,social_networks_grade=None):
	"""
	Returns a weighting from the indicated bar in the indicated month. 
	If the month is not specified, a global score is returned.
	"""
	con=sqlite3.connect(DB_PATH)
	cur=con.cursor()
	if month==None:
		data=cur.execute(f"select id_producto,sum(cantidad) from Prod_esta where id_establecimiento='{local}' group by id_producto;").fetchall()	
		samples=cur.execute(f"select count(DISTINCT year_month) from Prod_esta where id_establecimiento='{local}';").fetchone()[0]
	else:
		data=cur.execute(f"select id_producto,cantidad from Prod_esta where id_establecimiento='{local}' and year_month like '{month}%';").fetchall()
		samples=cur.execute(f"select count(DISTINCT year_month) from Prod_esta where id_establecimiento='{local}' and year_month like '{month}%';").fetchone()[0]

	con.close()

	if samples==0:
		return 0
	weight=sum(weightings[p[0]]*p[1] for p in data)
	if social_networks_grade==None:
		return weight/samples
	return social_networks_grade*SOCIAL_NETWORKS_WEIGHT+DATABASE_SALES_WEIGHT*weight/samples


def createColumns():
	"""
	Create the new columns of the table Establecimiento where the notes will be stored.
	"""
	con=sqlite3.connect(DB_PATH)
	cur=con.cursor()
	for m in months:
		cur.execute(f"alter table Establecimiento add column  Nota_{m} INTEGER;")	
	con.close()


def fromWeightToGrade(l):
	"""
	Performs a logarithmic conversion of the given list to convert the values on a scale from 0 to 10.
	"""
	grade_max=10
	grade_min=1
	max_value=max(l)
	if max_value==0:
		return [0 for i in range(len(l))]
	ret=[]
	for value in l:
		if value<0:
			ret.append(0)
		else:
			ret.append(grade_min+(grade_max-grade_min)*log(value+1)/log(max_value+1))
	return ret

	
if __name__ == '__main__':	
	try:
		createColumns()
	except:
		print("Current grades will be replaced")
	con=sqlite3.connect(DB_PATH)
	cur=con.cursor()
	bars=cur.execute("select id from Establecimiento;").fetchall()
	con.close()
	results=[[] for i in range(len(months))]
	
	for b in bars:
		bar=b[0]
		for i,month in enumerate(months):
			results[i].append(weightLocal(bar,month=month))

	grades=[]
	for result in results:
		grades.append(fromWeightToGrade(result))

	avg=fromWeightToGrade([weightLocal(bar[0],social_networks_grade=social_net[bar[0]]) for bar in bars])
	con=sqlite3.connect(DB_PATH)
	cur=con.cursor()
	
	for i,bar in enumerate(bars):
		cur.execute(f"update Establecimiento set average_grade={avg[i]} where id='{bar[0]}';")
		cur.execute(f"update Establecimiento set Nota_{months[0]}={grades[0][i]},Nota_{months[1]}={grades[1][i]},Nota_{months[2]}={grades[2][i]},Nota_{months[3]}={grades[3][i]},Nota_{months[4]}={grades[4][i]},Nota_{months[5]}={grades[5][i]},Nota_{months[6]}={grades[6][i]},Nota_{months[7]}={grades[7][i]},Nota_{months[8]}={grades[8][i]},Nota_{months[9]}={grades[9][i]},Nota_{months[10]}={grades[10][i]},Nota_{months[11]}={grades[11][i]} where id='{bar[0]}';")
	con.commit()
	con.close()


