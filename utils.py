from db import district_list

def create(dictionary):
    dictionary['id'] = max(item['id'] for item in district_list) + 1
    district_list.append(dictionary)

def retrieve(id):
    return next((item for item in district_list if item['id'] == id), None)

def update(id, name):
    next((item for item in district_list if item['id'] == id), None)['name'] = name

def delete(id):
    district_list[:] = [item for item in district_list if item['id'] != id]
