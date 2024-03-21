import random

print(random.randrange(1, 50))

#type conversion or typy casting 
#(1)implicit: something that is not clearly stated but well understood (2)explicit: this is something that is clearly stated

#explicit conversion 
float_string = '56.7'
print(float_string)
print(type(float_string))
converted = float(float_string)
print(converted)
print(type(converted))
new_int = int(converted)
print(new_int)

x = 3.6 + 3 
print(round(x))
print(str(x))
print(float(x))

y = 40.89+ 50
print(float(y))
print(round(y))
#g = 3.2e-12
#print(g)

#m = 300
#k = m
#print(id(m))
#print(id(k))

#for i in renge(128):
#    print(f"ASCII value:{i}, Character: {chr(i)}")
