import pandas as pd

df = pd.read_csv('/Users/tactlabs5/Documents/dev/tact/py-etl-csv-pg/source/people-100.csv')
print(df.to_string())