list_of_dicts = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 20}
]



sorted_list = sorted(list_of_dicts,key=lambda x:x['age'],)

print(sorted_list)
