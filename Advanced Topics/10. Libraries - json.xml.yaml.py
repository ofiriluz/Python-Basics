# Python has a built in libraries for jsom, xml and yaml handling
# It is very easy and very useful, since python has built in support for dicts
# Which can be easily serialized into different types like json
import json
# We can easily serialize and dump a dict into json and vice versa
some_dict = {'john': 23, 'alex': 25}
# This will dump the dict to a file
json.dump(some_dict, open("some_path", 'w'), indent=4)
# Will dump it into a string
json.dumps(some_dict)
# We can later on easily load the json into a dict
some_dict_loaded = json.load(open('some_path', 'r'))

# We can pretty much do the same idea for xml
from xml.dom import minidom

# parse an xml file by name
some_xml = minidom.parse('some_path.xml')

items = some_xml.getElementsByTagName('item')

# Get XML attributes
print(items[1].attributes['name'].value)
for elem in items:
    print(elem.attributes['name'].value)
# Get XML data
print(items[1].firstChild.data)
print(items[1].childNodes[0].data)
for elem in items:
    print(elem.firstChild.data)

# And same with yaml
import yaml

# Load and print the yaml as a dict
with open('items.yaml') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)
    print(data)
# Dump dict to yaml
users = [{'name': 'John Doe', 'occupation': 'gardener'},
         {'name': 'Lucy Black', 'occupation': 'teacher'}]
print(yaml.dump(users))