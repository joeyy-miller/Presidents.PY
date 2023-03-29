# Python program to read
# json file

import random
import json

# Opening JSON file
f = open('quotes.json')

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list
#data["orders"][0]["toppings"]
# for i in range(0,2):
#    print(data["presidents"][i]["quote"])

num = random.randint(1,55)
print(data['data'][num]['quote'])


# Closing file
f.close()