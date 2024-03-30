def id(dictionaries, myid):
    return [d for d in dictionaries if d['id'] == myid]

# Example usage:
data = [
    {'id': 1, 'name': 'Kannur'},
    {'id': 2, 'name': 'Malappuram'},
    {'id': 3, 'name': 'Kollam'},
    {'id': 4, 'name': 'Alappuzha'},
    {'id': 5, 'name': 'Kottayam'}
]

myid = 1
result = id(data, myid)

print(f"result: {result}")
