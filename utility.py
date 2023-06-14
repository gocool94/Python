import pandas as pd
import xml.etree.ElementTree as ET
import time
import pymysql
from sqlalchemy import create_engine
import requests
import logging
import psycopg2
import json
import pandas as pd
import concurrent.futures
from joblib import Parallel, delayed


#database connectivity

server = 'GOKULXY180\GOKUL_INSTANCE'
database = 'patient'
username = 'sa'
password = 'password_123'
conn_str = f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server"


def database_connection_1(df):
    engine = create_engine(conn_str)
    batch_size = 100000
    num_batches = len(df) // batch_size
    print(f"Batch split to {num_batches} counts.")
    for i in range(num_batches):
        print(f"Updating the {i} batch")
        start_idx = i * batch_size
        end_idx = (i + 1) * batch_size

        batch = df.iloc[start_idx:end_idx].copy()
        table_name = 'patients_detail'
        batch.to_sql(table_name, engine, if_exists='append', index=False)

def data_parsing(location):
    tree = ET.parse(location)

    root = tree.getroot()

    patients_data = []
    """for columns_elem in root.findall('columns'):
        patients_record = {}
        count = 0
        for column in columns_elem:
            if column.tag == 'patient_id':
                patients_record[column.tag] = column.text
            elif column.tag == 'patient_fname':
                patients_record[column.tag] = column.text
            elif column.tag == 'patient_lname':
                patients_record[column.tag] = column.text
            elif column.tag == 'patient_mname':
                patients_record[column.tag] = column.text
            elif column.tag == 'patient_gender':
                patients_record[column.tag] = column.text
            elif column.tag == 'patient_dob':
                patients_record[column.tag] = column.text
            elif column.tag == 'patient_mrn':
                patients_record[column.tag] = column.text
        patients_data.append(patients_record)"""

    for form in root.findall("./records/"):
        # print(form.attrib, form.text)
        patients_record = {}
        patients_record['patient_id'] = form.find('patient_id').text
        patients_record['patient_fname'] = form.find('patient_fname').text
        patients_record['patient_lname'] = form.find('patient_lname').text
        patients_record['patient_mname'] = form.find('patient_mname').text
        patients_record['patient_gender'] = form.find('patient_gender').text
        patients_record['patient_dob'] = form.find('patient_dob').text
        patients_record['patient_mrn'] = form.find('patient_mrn').text
        patients_record['Patients_id_value'] = None
        patients_record['isPatientPresent'] = None
        patients_data.append(patients_record)
        # print(form)
    df = pd.DataFrame(patients_data)

    #sdf = df.iloc[:10]
    print("Data parsing completed")
    return df
    # df.to_sql(name='patients_details', con=engine, if_exists='append', index=False)

def process_chunk(chunk):
    bearer_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJ1cm46b2lkOmZoaXIiLCJjbGllbnRfaWQiOiJkMzE5NDlhMi0zM2YwLTRjNWEtOWViNC02N2IzZDk4NTdhOTMiLCJlcGljLmVjaSI6InVybjplcGljOk9wZW4uRXBpYy1jdXJyZW50IiwiZXBpYy5tZXRhZGF0YSI6IkU1VFJ4X0tGX0Nqc3BfQVc0SU9WZnV5dFE4RWQtT3FrSENHSGVWeUpzaTNfZWdFbHZqc05wYkdQMWJHX0pRZVpwX0ItUFo5NWRiVzN6M2ROQ0pySHF1UUFwcld2aFViU1ZJRkZNQnpoTEhKVl9tSklrTkRpS0ZmdktEbTFsaGVjIiwiZXBpYy50b2tlbnR5cGUiOiJhY2Nlc3MiLCJleHAiOjE2ODU2MjE5MzEsImlhdCI6MTY4NTYxODMzMSwiaXNzIjoidXJuOm9pZDpmaGlyIiwianRpIjoiZjU0MzkxOGItMzgwMy00OWFjLTg4ZjQtYTgxNTRiM2UyYWU1IiwibmJmIjoxNjg1NjE4MzMxLCJzdWIiOiJldk5wLUtoWXdPT3FBWm4xcFoyZW51QTMifQ.Hn0xVcwHAH_leIbq4LvziD7TW65wnw1m45HUDx9o4Rg_pwQlXpkmOTgCPaGbZ480TW85v4niaZL_rodKo-uMa41YKVW4tIqayGYfMX7MfnDV_BWNMTfrD_QNi9PoQvy6IamJpG-ytwDEgkclyaB1PEGsCZR7ej1jniSwVAqYAaSz-2dFgYeZt4gLKzW9GEoi_0nptwrkRWnLUVnW8oitIJCuepkqy3HzK5GBefFQ-qjc7OOXFJKMv3JINoOJ80iAg9qoOkmAggTxdvnagB-oHaSCHWrN5apfG1zVaHE8c8xYiU0Wr_8-NHdnOSHwkCPwkiSxT4xFOTn4Cxaz5jsuPg"
    headers = {"Authorization": "Bearer " + bearer_token,
               "Accept": "application/json"}
    print("process is being started")
    for i in range(0, len(chunk)):
        patient_id = chunk.iloc[i, 0]
        patient_fname = chunk.iloc[i, 1]
        patient_lname = chunk.iloc[i, 2]
        patient_mname = chunk.iloc[i, 3]
        patient_gender = chunk.iloc[i, 4]
        patient_dob = str(chunk.iloc[i, 5])
        patient_mrn = chunk.iloc[i, 6]

        re = requests.get(
            "https://fhir.epic.com/interconnect-fhir-oauth/api/FHIR/R4/Patient?birthdate=" + patient_dob + "&family=" + patient_lname + "&gender=" + patient_gender + "",
            headers=headers)
        # get the status code
        #print(re.status_code)
        while (re.status_code == 401):
            time.sleep(10)
            headers = get_connection(input("Enter the bearer token:--"))
            # bearer token get here
            re = requests.get(
                "https://fhir.epic.com/interconnect-fhir-oauth/api/FHIR/R4/Patient?birthdate=" + patient_dob + "&family=" + patient_lname + "&gender=" + patient_gender + "",
                headers=headers)

        str_data = re.content.decode('utf-8')

        # Convert string to Python object
        python_obj = json.loads(str_data)

        # Convert Python object to JSON string
        json_data = json.dumps(python_obj)
        #print(json_data)

        p_value = python_obj["total"]
        #print(p_value)
        patient_entry = python_obj.get('entry', [])[0]
        # Assumes only one patient entry

        if p_value >= 1:
            patient_resource = patient_entry.get('resource', {})
            patient_id = patient_resource.get('id')
            #print(patient_id)
            chunk.iloc[i, 7] = patient_id

            chunk.iloc[i, 8] = "true"

        else:
            chunk.iloc[i, 7] = 0
            chunk.iloc[i, 8] = 'false'
        print(f"Completed {i} of {len(chunk)}")
        #print(chunk)
    return chunk

def get_connection(bearer_token):

    headers = {"Authorization": "Bearer " + bearer_token,
               "Accept": "application/json"}
    return headers

# Create a DataFrame

# Define the number of chunks and the size of each chunk



if __name__ == '__main__':
    df = data_parsing(r"C:\Users\Gokul\Downloads\TestEHRTwoMillion.xml")
    print("Database is getting updated")
    # database_connection(sdf)
    start = time.time()
    print(start)
    print(23 * 2.3)
    database_connection_1(df)
    end = time.time()
    print(end)
    print(end - start)
    elapsed_time = end - start
    minutes = int(elapsed_time // 60)
    seconds = int(elapsed_time % 60)
    # Print the elapsed time
    print(f"Elapsed time: {minutes} minutes {seconds} seconds")
    print("update completed")
    bearer_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJ1cm46b2lkOmZoaXIiLCJjbGllbnRfaWQiOiJkMzE5NDlhMi0zM2YwLTRjNWEtOWViNC02N2IzZDk4NTdhOTMiLCJlcGljLmVjaSI6InVybjplcGljOk9wZW4uRXBpYy1jdXJyZW50IiwiZXBpYy5tZXRhZGF0YSI6IkU1VFJ4X0tGX0Nqc3BfQVc0SU9WZnV5dFE4RWQtT3FrSENHSGVWeUpzaTNfZWdFbHZqc05wYkdQMWJHX0pRZVpwX0ItUFo5NWRiVzN6M2ROQ0pySHF1UUFwcld2aFViU1ZJRkZNQnpoTEhKVl9tSklrTkRpS0ZmdktEbTFsaGVjIiwiZXBpYy50b2tlbnR5cGUiOiJhY2Nlc3MiLCJleHAiOjE2ODU2MjE5MzEsImlhdCI6MTY4NTYxODMzMSwiaXNzIjoidXJuOm9pZDpmaGlyIiwianRpIjoiZjU0MzkxOGItMzgwMy00OWFjLTg4ZjQtYTgxNTRiM2UyYWU1IiwibmJmIjoxNjg1NjE4MzMxLCJzdWIiOiJldk5wLUtoWXdPT3FBWm4xcFoyZW51QTMifQ.Hn0xVcwHAH_leIbq4LvziD7TW65wnw1m45HUDx9o4Rg_pwQlXpkmOTgCPaGbZ480TW85v4niaZL_rodKo-uMa41YKVW4tIqayGYfMX7MfnDV_BWNMTfrD_QNi9PoQvy6IamJpG-ytwDEgkclyaB1PEGsCZR7ej1jniSwVAqYAaSz-2dFgYeZt4gLKzW9GEoi_0nptwrkRWnLUVnW8oitIJCuepkqy3HzK5GBefFQ-qjc7OOXFJKMv3JINoOJ80iAg9qoOkmAggTxdvnagB-oHaSCHWrN5apfG1zVaHE8c8xYiU0Wr_8-NHdnOSHwkCPwkiSxT4xFOTn4Cxaz5jsuPg"
    headers = {"Authorization": "Bearer " + bearer_token,
               "Accept": "application/json"}

    #headers = get_connection(input("Enter the bearer token:--"))
    num_chunks = 10
    print(num_chunks)
    chunk_size = len(df) // num_chunks
    print(chunk_size)
    chunks = [df[i:i + chunk_size].copy() for i in range(0, len(df), chunk_size)]
    #print(chunks)
    processed_chunks = Parallel(n_jobs=-1)(delayed(process_chunk)(chunk) for chunk in chunks)
    combined_df = pd.concat(processed_chunks)
    print(combined_df)
    database_connection_1(combined_df)






