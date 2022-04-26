import sqlite3
import pandas as pd
from sqlalchemy import exc
conn=sqlite3.connect(r'O:\VSCODE-Django\mysite3\db.sqlite3')
df = pd.read_csv(r'O:\VSCODE-Django\mysite3\book.csv', encoding='utf-8',sep=',')
print(df)
try:
    df.to_sql('book', conn, if_exists='append', index=False) #append
except exc.IntegrityError:
    #Ignore duplicates
    pass
conn.close()