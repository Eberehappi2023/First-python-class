car = {
    'brand':'Toyota',
    'model':'spider',
    'year': 2020,
    'color': ['ash','red','black']
}
print(car)
print(car['brand'])
print(car.get('color'))
print(car.keys())
car['year'] = 2023
print(car)
print(car.values())
print(car.items())
if 'year' in car:
    print("yes, 'year' is one of the keys in the car dictionary")


car.update({'engines':'v6'})
print(car)
#car.pop('color')
#print(car)
#car.popitem()
#print(car)
#del car
#print(car)
#loop through value
for x in car:
    print(car[x])

for c in car.values():
    print(c)

for a in car.keys():
    print(a)

for m in car.items():
    print(m)
carr = {'brands': 'lexus'}
carr = car.copy()
print(carr)

cars = dict(carr)
print(cars)

python_class = {
  "student1" : {
    "name" : "John",
    "age" : 17,
    "course": 'Ethical hacking',
    "complexion": "caramel"
  },
 "student2" : {
    "name" : "Mummy Happy",
    "age" : 19,
    "course": 'Data analysis',
    "complexion": "dark"
  },
  "student3" : {
    "name" : "Rejoice",
    "age" : 17,
    "course": 'cybersecurity',
    "complexion": "yellow"
  },
  "student4" : {
    "name" : "Justic",
    "age" : 12,
    "course": 'cybersecurity',
    "complexion": "Fair"
  },
  "student5" : {
    "name" : "Chigemezu",
    "age" : 17,
    "course": 'Marketing',
    "complexion": "yellow"
  },
  "student6" : {
    "name" : "michael",
    "age" : 24,
    "course": 'cybersecurity',
    "complexion": "dark"
  },
  "student7" : {
    "name" : "Roy",
    "age" : 22,
    "course": 'cybersecurity',
    "complexion": "Dark"
  }
}
print(python_class.items())

for x in python_class.items():
    print(x)