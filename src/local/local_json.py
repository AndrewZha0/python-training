import json

# 对象转json
list_data = [{"name": "tom", "age": 18}, {"name": "jerry", "age": 20}, {"name": "haven", "age": 16}]
json_dumps = json.dumps(list_data)
print(type(json_dumps))
print(json_dumps)

# json转对象
str_data = '[{"name": "tom", "age": 18}, {"name": "jerry", "age": 20}, {"name": "haven", "age": 16}]'
json_loads = json.loads(str_data)
print(type(json_loads))
print(json_loads)
