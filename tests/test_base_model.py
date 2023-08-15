#!/usr/bin/python3
"""Import Models for test"""
from models.base_model import BaseModel

new_model = BaseModel()
new_model.name = "My First Model"
new_model.my_number = 89
print(new_model)
new_model.save()
print(new_model)
my_model_json = new_model.to_dict()
print(my_model_json)
print("JSON of new_model:")
for key in my_model_json.keys():
    x = type(my_model_json[key])
    print("\t{}: ({}) - {}".format(key, x, my_model_json[key]))
