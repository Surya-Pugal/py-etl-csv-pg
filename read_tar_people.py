# source: https://www.w3schools.com/python/pandas/pandas_csv.asp
# https://medium.com/analytics-vidhya/part-4-pandas-dataframe-to-postgresql-using-python-8ffdb0323c09
# https://hasura.io/learn/database/postgresql/installation/2-postgresql-connection-string/
# https://datatofish.com/concatenate-values-python/
# https://www.tutorialkart.com/postgresql/postgresql-delete-column/
# https://www.educative.io/answers/how-to-delete-a-column-in-pandas


import tarfile
import pandas as pd
import psycopg2
from sqlalchemy import create_engine
from pandas import DataFrame 


# doublw underscore variables
print(__path__)
print(__file__)



#Extracted tar files has 2 csv files 
def extract_tar_file(tar_file_path, destination_dir):
    tar = tarfile.open(tar_file_path,'r')
    print("read zip files: ", tar.list())
    tar.extractall(destination_dir)
    tar.close




# python script to Load/read the CSV into a pandans DataFrame:
def read_csv():
    df = pd.read_csv('/Users/tactlabs5/Documents/dev/tact/py-etl-csv-pg/source/people-100.csv')
    print(df.to_string())
    
    
     # concatenate the first name and last name columns into a single column(Full name)
    df ['Full Name'] = df['First Name'] + " " + df['Last Name']
    print(df)
    
    # df.drop(['First Name', 'Last Name'], axis=1, inplace=True)
    print("The pandas dataframe after dropping the first and last name columns: ")
    print(df)


    conn_string = 'postgresql://postgres:root@localhost:5432/postgres'
    print("Data base connected")
# db = create_engine(conn_string)
# con = db.connect()
   
# Save the data from dataframe to
# postgres table "pepole-100"
    df.to_sql('people-100', conn_string, if_exists='append', index=False)
    # Not copying over the index
    
 
    


# if __name__ == '__main__':
    # extract_tar_file('/Users/tactlabs5/Documents/dev/tact/py-etl-csv-pg/source/CsvSamples.tar.gz', '/Users/tactlabs5/Documents/dev/tact/py-etl-csv-pg/destination')
    # read_csv()