num1 = 42   # variable declaration, initialize number
num2 = 2.3  # variable declaration, initialize number
boolean = True  # variable declaration, initialize boolean
string = 'Hello World' #variable declaration, initialize string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']      # variable declaration, initialize list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}      # variable declaration, initialize dictionary
fruit = ('blueberry', 'strawberry', 'banana')      #variable declaration, initialize tuple
print(type(fruit))      # log statement, type check
print(pizza_toppings[1])    # log statement, list access value
pizza_toppings.append('Mushrooms')  # log statement, list add value
print(person['name'])       # log statement, dictionary access value
person['name'] = 'George'   # dictionary change value
person['eye_color'] = 'blue'    # dictionary change value
print(fruit[2])     # log statement, tuple access value

if num1 > 45:           # if statement
    print("It's greater")   # log statement
else:           # else statement
    print("It's lower")     # log statement

if len(string) < 5:     # if statement, length check
    print("It's a short word!")     # log statement
elif len(string) > 15:      # else if statement, length check
    print("It's a long word!")      # log statement
else:       # else statement, length check
    print("Just right!")    # log statement

for x in range(5):      # for loop start
    print(x)            # log statement, for loop stop
for x in range(2,5):    # for loop start
    print(x)            # log statement, for loop stop
for x in range(2,10,3):     # for loop start, for loop increment (by 3 between 2 and 10)
    print(x)            # log statement, for loop stop
x = 0                   # variable declaration
while(x < 5):           # while loop start
    print(x)            # log statement, while loop stop
    x += 1              # while loop increment

pizza_toppings.pop()        # list delete value
pizza_toppings.pop(1)       # list delete value

print(person)       # log statement
person.pop('eye_color')     # dictionary delete value (attempt), KeyError: 'eye_color'
print(person)   # log statement

for topping in pizza_toppings:      # for loop start, variable declaration
    if topping == 'Pepperoni':      # if statement
        continue                    # for loop continue
    print('After 1st if statement')     # log statement
    if topping == 'Olives':         # if statement
        break                       # for loop break

def print_hello_ten_times():        # function
    for num in range(10):           # for loop start, variable declaration
        print('Hello')              # log statement

print_hello_ten_times()             # function return

def print_hello_x_times(x):         # function parameter, variable declaration
    for num in range(x):            # for loop start
        print('Hello')              # log statement

print_hello_x_times(4)              # function return, function argument

def print_hello_x_or_ten_times(x = 10):     # function, variable declaration, function parameter
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()            # function return
print_hello_x_or_ten_times(4)           # function return, function argument


"""
Bonus section
"""

# print(num3)           # NameError: name num3 is not defined
# num3 = 72           # variable declaration
# fruit[0] = 'cranberry'        # TypeError: 'tuple' object does not support item assignment
# print(person['favorite_team'])    # KeyError: 'favorite_team'
# print(pizza_toppings[7])      # IndexError: list index out of range
#   print(boolean)      # IndentationError: unexpected indent
# fruit.append('raspberry')     # AttributeError: 'tuple' object has no attribute 'append'
# fruit.pop(1)      # AttributeError: 'tuple' object has no attribute 'pop'