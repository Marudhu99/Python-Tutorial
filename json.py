import json

json_string = '{"name": "Marudhu", "age": 23}'

# Parse JSON
parsed_json = json.loads(json_string)
age = parsed_json["age"]

print("Age:", age)


# Convert from Python to JSON
person = {"name": "Marudhu", "age": 23}

# convert into json
y = json.dumps(person)
print(y)