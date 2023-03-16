# sources: https://stackoverflow.com/questions/33481974/importerror-no-module-named-pandas
# https://www.w3schools.com/python/pandas/pandas_csv.asp
# source: https://www.geeksforgeeks.org/how-to-insert-a-pandas-dataframe-to-an-existing-postgresql-table/
# https://hasura.io/learn/database/postgresql/installation/2-postgresql-connection-string/
# https://stackoverflow.com/questions/62688256/sqlalchemy-exc-nosuchmoduleerror-cant-load-plugin-sqlalchemy-dialectspostgre
# https://apoor.medium.com/quickly-load-csvs-into-postgresql-using-python-and-pandas-9101c274a92f

import psycopg2
import pandas as pd
from sqlalchemy import create_engine


# Instantiate sqlachemy.create_engine object
conn_string = 'postgresql://postgres:root@localhost:5432/postgres'

# pythonn = db.connect()
print("Data base connected...")

# read the csv in to pandas dataframe
df = pd.read_csv('organizations-100.csv')
# str = df.tostring()
print(df)

# Save the data from dataframe to
# postgres table "organization_data"

df.to_sql(
    'organization_data', 
    conn_string,
    if_exists='append',
    index=False # Not copying over the index
)