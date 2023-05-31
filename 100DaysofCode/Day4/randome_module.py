import random

print(random.randint(100,200))

# -> 147

#different random number in float

random_float = random.random() * 5

print(random_float)

import requests

mm = requests.get("https://fhir-open.cerner.com/r4/ec2458f2-1e24-41c8-b71b-0e701af7583d/Patient?birthdate=1973-06-03&family=Lin&given=Derrick&gender=male")
print(mm)