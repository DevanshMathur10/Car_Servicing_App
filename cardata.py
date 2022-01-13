import mysql.connector as sql
import os
con=sql.connect(user=os.environ.get('SQLNAME'),password=os.environ.get('SQLPASS'),host=os.environ.get('SQLHOST'),database="automotives")
c=con.cursor()
companylist=[
"Maruti Suzuki",
"Hyundai Motors",
"Tata Motors",
"Toyota",
"Kia Motors",
"Skoda",
"MG",
"Mercedes Benz",
"Volkswagen",
"Honda",
"Renault",
"Mahindra",
"BMW",
"Jeep",
'Ford',
"Nissan",
'Audi',
'Datsun',
"Tesla"
]

carslist=[
'Model S',
'Model 3'
]
for i in carslist:
  add_last_name = ("""INSERT INTO cars 
                (company,model) 
                VALUES (%(company)s,%(model)s)""")
  data_last_name = {
    'company': companylist[18],
    'model':i
  }
  c.execute(add_last_name, data_last_name)
con.commit()
con.close()

