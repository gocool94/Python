import mysql.connector
import pandas as pd

# Connect to the database
mydb = mysql.connector.connect(host='localhost',password='password',user='root',database="patientdb")


# Create a DataFrame
df = pd.DataFrame({
  'Name': ['Alice', 'Bob', 'Charlie'],
  'Age': [25, 30, 35]
})

# Create the table if it doesn't exist
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS patient (Name VARCHAR(255), Age INT)")

# Save the DataFrame to the database
df.to_sql(name='patient', con="patientdb", if_exists='append', index=False)

# Close the database connection
mydb.close()
