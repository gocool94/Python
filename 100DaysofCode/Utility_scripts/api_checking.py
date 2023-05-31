import requests


import json

def get_connection(bearer_token):

    headers = {"Authorization": "Bearer " + bearer_token,
               "Accept": "application/json"}
    return headers



re = requests.get("https://fhir.epic.com/interconnect-fhir-oauth/api/FHIR/R4/Patient?birthdate=1993-08-18&family=Davis&gender=male",headers=headers)

re.content
str_data = re.content.decode('utf-8')

# Convert string to Python object
python_obj = json.loads(str_data)

# Convert Python object to JSON string
json_data = json.dumps(python_obj)
print(json_data)

print(python_obj["total"])
patient_entry = python_obj.get('entry', [])[0]
# Assumes only one patient entry

if patient_entry >= 1:
    patient_resource = patient_entry.get('resource', {})
    patient_id = patient_resource.get('id')
    print(patient_id)





