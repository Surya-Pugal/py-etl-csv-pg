# py-etl-csv-pg
# The to_sql() function is used to write records stored in a DataFrame to a SQL database.

# push pandas to postgres
# https://hasura.io/learn/database/postgresql/installation/2-postgresql-connection-string/

# https://datatofish.com/concatenate-values-python/(map(string)--  contains a combination of integers and strings)

# query to remove a column from a postgres table
ALTER TABLE public."people-100"
	DROP COLUMN "Last Name";

# query to remove a column
<!-- https://www.educative.io/answers/how-to-delete-a-column-in-pandas -->

# overall work
pandas is a python library, used to read the csv, text, json files and read into data feame(nothing but rows and columns) and push the data in to any data base like postgres.