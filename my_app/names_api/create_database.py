import os
from names_api.models import Person

def create_default_database():
    file_with_names = open(os.path.dirname(os.path.realpath(__file__)) + '/names.txt', "r")
    names_dict = {}

    name_index = 0
    for line in file_with_names:
        names_dict[name_index] = {
            'name': line.strip('\n'),
            'last_name': ''
        }
        name_index += 1

    for person_id in names_dict:
        Person.objects.create(
            name=names_dict[person_id]['name'],
            last_name=names_dict[person_id]['last_name']
        )
