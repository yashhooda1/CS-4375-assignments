# -*- coding: utf-8 -*-
"""Python Crash Course.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-QIzSOS-zyi3PL1hBriEluWcrQUTEqcI
"""

# Python Crash Course <esc> MM Ctrl-Enter

# Data Types 
# Numbers

1+1

2 ** 4

5 % 2

(2+3) * (5+5)

# Variable Assignment

name_of_var = 2

name_of_var

x = 2
y = 3
z = x + y
z

x = 3
x
x = 'hello'
x

x = 3
print(x)
x = 'hello'
x

num = 12
name = 'Sam'
print('My number is: {one}, and my name is: {two}'.format(one=num, two=name))

print(f'My number is: {num}, and my name is: {name}')

num = 12
name = "Sam"
print("My number is: {one}, and my name is: {two}".format(one=num, two=name))

# Lists
[1,2,3]

['hi', 1, [1,2]]

my_list = ['a', 'b', 'c']

my_list.append('d')

my_list

name = 'Khan'

type(name)

name = "Khan"
type(name)

my_list[0]

my_list[1:]

my_list[:1]

my_list[0] = 'NEW'
my_list

nest = [1,2,3,[4,5,['costco', 'target']]]

nest[3]

nest[3][2][1]

# Dictionaries

d = {'key1':'item1','key2':'item'}

d

type(d)

True

t = (1,2,3)

t[0]

t[0] = 'New'

t[0] = 5

1 > 2

1 == 1

( 1 > 2) and (2 < 3)

(1 == 2) or (2 == 3) or (4 == 4)

if 1 < 2:
  print('Yep!')

if 1 > 2:
  print('Yep!')
else:
  print('Not Yep!')

if 1 == 2:
  print('first')
elif 3 == 3:
  print('middle')
else:
  print('last')

seq = [1,2,3,4,5]
for item in seq:
  print(item)

for jelly in seq:
  print(jelly+jelly)

i=1
while i<5:
  print('i is: {}'.format(i))
  i = i+1

range(5)

for i in range(5):
  print(i)

list(range(5))

x = [1,2,3,4]
out = []
for item in x:
  out.append(item**2)
print(out)

[item**2 for item in x]



def my_func(param1='default'):
  print(param1)

my_func()

my_func('Python')

def square(x):
  return x**2
out = square(2)
out

seq

def times2(var):
  return var*2

map(times2, seq)

list(map(times2, seq))

st = 'hello my name is Sam'
print(st.lower())
st.upper()

lambda var: var*2

list(map(times2, seq))

list(map(lambda var: var*2, seq))

list(filter(lambda item: item%2, seq))

list(filter(lambda item: item%2 == 0, seq))

seq

st

st.split()

tweet = 'Go Sprots! #Sports'
tweet.split('#')

tweet.split('#')[1]

d

d.keys()

d.items()

lst = [1,2,3]
lst.pop()

'x' in [1,2,3]

'x' in ['x', 1, 2]
