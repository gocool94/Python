import psycopg2
import pandas as pd
from sqlalchemy import create_engine



hostname = 'localhost'
database = 'postgres'
username = 'postgres'
pwd = 'password'
port_id = 5432

data = {
    'id':[1,2,3],
    'name': ['Alice', 'Bob', 'Charlie'],
        'salary': [25, 30, 35],
        'city': ['New York', 'San Francisco', 'Chicago']}
df = pd.DataFrame(data)


try:
    conn = psycopg2.connect(host = hostname,dbname = database,user=username,password = pwd,port = port_id)

    cur = conn.cursor()

    engine = create_engine('postgresql://postgres:password@localhost:5432/postgres')

    create_script = '''
    
    CREATE TABLE IF NOT EXISTS employee (
    id int PRIMARY KEY,
    name varchar(40) NOT NULL,
    salary int,
    dept_id varchar(30)
    )
    
    '''
    cur.execute(create_script)

    df.to_sql(name='employee', con=engine, if_exists='replace', index=False)


    conn.commit()
except Exception as error:
    print(error)

finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()



