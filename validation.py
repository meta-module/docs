#!/usr/bin/env python3
import json
from jsonschema import validate

# load schema
# Describe what kind of json you expect.
with open('schema/environment.json', 'r') as json_file:
    schema = json.load(json_file)

# read json file
with open('metamodule/environment.json', 'r') as json_file:
    data = json.load(json_file)

# Validate will raise exception if given json is not
# what is described in schema.


try:
    validate(instance=data, schema=schema)
except jsonschema.exceptions.ValidationError as ex:
    print(ex)

# print for debug
print(data)