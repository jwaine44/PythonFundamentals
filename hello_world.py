# 1. TASK: print "Hello World"
print("Hello World")
# 2. print "Hello Noelle!" with the name in a variable
name = "Noelle"
print("Hello", name, "!")	# with a comma
print("Hello " + name + "!")	# with a +
# 3. print "Hello 42!" with the number in a variable
name = 42
print("Hello", name, "!")	# with a comma
print("Hello" + name + "!")	# with a +	-- this one should give us an error!
print("Hello " + str(name) + "!")              # NINJA BONUS: Figure out how to resolve the error from above, without changing the + sign to a comma
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print("I love to eat {} and {}".format(fave_food1, fave_food2)) # with .format()
print(f"I love to eat {fave_food1} and {fave_food2}") # with an f string

experimental_string = "This is a test string"
print(experimental_string.upper())
print(experimental_string.lower())
print(len(experimental_string))