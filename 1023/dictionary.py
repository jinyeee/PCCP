dic = {
    'name' : 'jun',
    'age' : 18,
    'gender' : 'M'
}
dic['name']

dic['height'] = 188

for key in dic:
    print(key)
    print(dic[key])

print()
for value in dic.values():
    print(value)

print()
for key in dic.keys():
    print(key)

print()
for key, value in dic.items():
    print(key, value)



