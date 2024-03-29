#If you have a Python object, you can convert it into a JSON string
#by using the json.dumps() method.

import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)
y1 = json.loads(y)
# the result is a JSON string:
print(y1["city"])