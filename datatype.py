x = "Hello World"
print(type(x))
#int
number = 10
print(number)
print(type(number))

# float
float_num = 23.4
print(float_num)
print(type(float_num))

# compex
complex_num = 23j
print(complex_num)
print(type(complex_num))

#list
cars = ["G-wagon", "Audi", "toyot"]
print(cars)
print(type(cars))

#tuple
afro_beats_artists = ("Burna girl", "Davido", "Tacno", "Lyta")
print(afro_beats_artists)
print(type(afro_beats_artists))

#Renge
range_num =  (8)
print(range_num)
print(type(range_num))

#dict
student_info = {'name':'happiness',
                'age':'20',
                'stack':'Python',
                'level':'Entry'}
print(student_info)
print(type(student_info))

#set
cooking_set = {'knife', 'plate', 'plate','pot', 'spoon', 'stove'}
print(cooking_set)
print(type(cooking_set))

#frozonset
frozon_set = frozenset({1,2,3,4,5,6,7,8,9,10})
print(frozon_set)
print(type(frozon_set))

#boolean
a = True
print(a)
print(type(a))
b = False
print(b)
print(type(b))

#bytes
x = b'Hello'
print(x)
print(type(x))

y = bytearray(5)
print(y)
print(type(y))

z = memoryview(bytes(5))
print(z)
print(type(z))

floating_num = 455. 
print(floating_num)
print(type(floating_num))

f = 35e4
print(f)
g = 12E3 
print(g)

h = 674.54e1
print(h)

print(3j + 5)

print(4/2)


num1 = 45
num2 = 23.99
print(float(num1 + num2))
print(int(num2))
print(complex(num2))

def greet():
    print('Hello World')

greet()