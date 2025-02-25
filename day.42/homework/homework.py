my_dict = {'name': 'Ahmed', 'age': 25, 'city': 'New York', 'job': 'Engineer', 'hobby': 'Reading'}
print(my_dict.keys())

my_dict2 = {'name': 'Bobinski', 'age': 30, 'city': 'San Francisco'}
print(my_dict2.values())

my_dict3 = {'name': 'wupaka', 'age': 28, 'city': 'Boston'}
print(my_dict3.items())

for key, value in my_dict3.items():
    print(key, value)

my_dict4 = {'name': 'Davida', 'age': 35, 'city': 'Chicago'}
print('age' in my_dict4)

print(my_dict4.get('job', 'Not found'))

my_dict4['job'] = 'Doctor'
print(my_dict4)

my_dict4.pop('city')
print(my_dict4)

my_dict5 = {'name': 'Evelyn', 'age': 40}
my_dict4.update(my_dict5)
print(my_dict4)

my_dict6 = {'name': 'Frankinstein', 'age': 45, 'city': 'Miami'}
print(len(my_dict6))