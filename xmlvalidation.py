import threading
import xml.etree.ElementTree as ET
import pymysql

# Set the path to the XML file
xml_file = "C:\Users\Gokul\Downloads\TestEHRTwoMillionOutput2000.xml"

# Define the database connection details
db_host = "localhost"
db_user = "username"
db_password = "password"
db_name = "database_name"

# Create a function to process each record and insert into database
def process_record(record):
    # Extract data from the record
    for record in root:
        # Access the child elements of the record
        for child in record:
            # Access the child elements of the child elements of the record
            for subchild in child:
                # Do something with the subchild elements
                print(subchild.tag, subchild.text)
    # ... and so on for other tags

    # Insert the data into the database
    """
    db = pymysql.connect(host=db_host, user=db_user, password=db_password, database=db_name)
    cursor = db.cursor()
    sql = "INSERT INTO table_name (tag1, tag2, tag3) VALUES (%s, %s, %s)"
    values = (tag1, tag2, tag3)
    cursor.execute(sql, values)
    db.commit()
    db.close()
    """

def process_batch(start_index, end_index):
    # Load the XML file and get a list of all the record elements
    tree = ET.parse(xml_file)
    root = tree.getroot()
    records = root.findall("record")

    # Process each record in the batch
    for i in range(start_index, end_index):
        record = records[i]
        process_record(record)

# Set the number of threads to use
num_threads = 4

# Load the XML file and get the total number of records
tree = ET.parse(xml_file)
root = tree.getroot()
num_records = len(root.findall("record"))

# Number of record in each batch
batch_size = num_records // num_threads

# Threa for each batch
threads = []
for i in range(num_threads):
    start_index = i * batch_size
    end_index = start_index + batch_size
    if i == num_threads - 1:
        end_index = num_records
    thread = threading.Thread(target=process_batch, args=(start_index, end_index))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
