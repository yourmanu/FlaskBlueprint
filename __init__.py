import json
s='{"name": "Shiva","age":50}'

h='{"name": "shivakumar", "n": 9}'

j=json.loads(h)
print(j['name'])
print(j)

s={
    "name": "Shiva"
}

print(s['name'])