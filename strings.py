greeting = 'Good afternoon'
print(len(greeting))

print(greeting[3])

#Loop through the letters in the word "good afternoon":
for each_element in greeting:
    print(each_element)
#slicing string
fruit = "mango"
print(fruit[0:3])
print(fruit[2:5])
print(fruit[:])
#steps in slicing 
#[start:stop]
#[start:stop:step]
#Negetiv index
#Omitting index
a = 'hello world'
print(a[::-1])
print(a[0:])
#concatenation
b = 'Hello'
c = 'World'
d = b+c
print(b+c)
print(b+' '+c)
#formatting string
a = 'Hello'
b = 'World'
print(f'Greeting {a} {b}')
#format string literal
#.format()method
print(a.upper())
no_of_students = 17
age = 20
fruits = ['mango', 'orange']
python_class = "There are interms {no_of_students} in python class. {} {}"
#print(python_class.format(age, fruit, no_of_students))
print(f'there are {no_of_students} interms in python \\class. \nwho are all {age} years old')