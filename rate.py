"""
Computes the grade of each local according to data stored in the database. 
"""

import sqlite3
from weightings import weightings
from math import log

DB_PATH='damm.bd'
months=["Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Sep","Oct","Nov","Dec"]


def weightLocal(local,month=None):
	"""
	Returns a weighting from the indicated bar in the indicated month. 
	If the month is not specified, a global score is returned.
	"""
	con=sqlite3.connect(DB_PATH)
	cur=con.cursor()
	try: #Treure
		if month==None:
			data=cur.execute(f"select codigo_producto,sum(cantidad) from Prod_esta where nombre_establecimiento='{local}' group by codigo_producto;").fetchall()	
			samples=cur.execute(f"select count(DISTINCT año_mes) from Prod_esta where nombre_establecimiento='{local}';").fetchone()[0]
		else:
			data=cur.execute(f"select codigo_producto,cantidad from Prod_esta where nombre_establecimiento='{local}' and año_mes like '{month}%';").fetchall()
			samples=cur.execute(f"select count(DISTINCT año_mes) from Prod_esta where nombre_establecimiento='{local}' and año_mes like '{month}%';").fetchone()[0]
	except:
		con.close()
		return 0
	con.close()
	weight=0
	
	if samples==0:
		return 0
	weight=sum(weightings[p[0]]*p[1] for p in data)
	return weight/samples


def createColumns():
	"""
	Create the new columns of the table Establecimiento where the notes will be stored.
	"""
	con=sqlite3.connect(DB_PATH)
	cur=con.cursor()
	cur.execute(f"alter table Establecimiento add column Nota_Total INTEGER;")
	for m in months:
		cur.execute(f"alter table Establecimiento add column  Nota_{m} INTEGER;")	
	con.close()


def fromWeightToGrade(l):
	"""
	Performs a logarithmic conversion of the given list to convert the values on a scale from 0 to 10.
	"""
	grade_max=10
	grade_min=0
	min_value=min(l)
	max_value=max(l)
	if max_value==0:
		return [0 for i in range(len(l))]
	ret=[]
	for value in l:
		if value<0:
			ret.append(0)
		else:
			ret.append(10*log(value+1)/log(max_value+1))
	return ret




if __name__ == '__main__':	
	try:
		createColumns()
	except:
		print("Current grades will be replaced")
	con=sqlite3.connect(DB_PATH)
	cur=con.cursor()
	bars=cur.execute("select nombre from Establecimiento;").fetchall()
	con.close()
	results=[[] for i in range(len(months))]
	
	for b in bars:
		bar=b[0]
		for i,month in enumerate(months):
			results[i].append(weightLocal(bar,month))

	grades=[]
	for result in results:
		grades.append(fromWeightToGrade(result))

	con=sqlite3.connect(DB_PATH)
	cur=con.cursor()
	for i,bar in enumerate(bars):
		try: #Treure
			cur.execute(f"update Establecimiento set Nota_{months[0]}={grades[0][i]},Nota_{months[1]}={grades[1][i]},Nota_{months[2]}={grades[2][i]},Nota_{months[3]}={grades[3][i]},Nota_{months[4]}={grades[4][i]},Nota_{months[5]}={grades[5][i]},Nota_{months[6]}={grades[6][i]},Nota_{months[7]}={grades[7][i]},Nota_{months[8]}={grades[8][i]},Nota_{months[9]}={grades[9][i]},Nota_{months[10]}={grades[10][i]},Nota_{months[11]}={grades[11][i]} where nombre='{bar[0]}';")
			con.commit()
		except:
			pass
	cur.execute(f"update Establecimiento set Nota_Total=(Nota_{months[0]}+Nota_{months[1]}+Nota_{months[2]}+Nota_{months[3]}+Nota_{months[4]}+Nota_{months[5]}+Nota_{months[6]}+Nota_{months[7]}+Nota_{months[8]}+Nota_{months[9]}+Nota_{months[10]}+Nota_{months[11]})/12;")
	con.commit()
	con.close()