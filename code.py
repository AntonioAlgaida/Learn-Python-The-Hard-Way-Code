# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 08:25:44 2018

@author: AntonioGuillen
"""

#%%
# =============================================================================
# Exercise 1 - Hello Word
# =============================================================================

print("Hola holita vecinito")
print("En python3 a la hora de")
print("imprimir por pantalla")
print(""" se utiliza print("TEXTO") """)
print("y además, si se quiere meter un texto")
print("que incluya comillas, se utiliza la comilla triple")

print("I'd much rather you 'not'.")
print('I "said" do not touch this .')

#%%
# =============================================================================
# Exercise 2 - Comments and Pound Characters
# =============================================================================

# A comment, this is so you can read your program later.
# Anything after the # is ignored by python.

print("I could have code like this.") # and the comment after is ignoredç

# You can also use a comment to "disable" or comment out a piece of code:
# print("This won't run.")

print("This will run.")




#%%
# =============================================================================
# Exercise 3 - Numbers and Math
# =============================================================================

print("I will now count my chickens:")

print("Hens",25.0+30.0/6.0)
print("Roosters", 100.0-25.0*3.0%4.0)

print("Now I will count the eggs:")

print(3.0+2.0+1.0-5.0+4.0%2.0-1.0/4.0+6.0)

print("Is this true that 3+2<5-7?")

print(3+2 < 5-7)

print("What is 3+2",3+2)


#%%
# =============================================================================
# Exercise 4 - Variable and Names
# =============================================================================
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven*space_in_a_car
average_passenger_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have",passengers,"to carpool today.")
print("We need to put about",average_passenger_per_car,"in each car.")


#%%
# =============================================================================
# Exercise 5 - More Variables and Printing
# =============================================================================
my_name = "Antonio"
my_surname = 'Guillen'
my_age = 24
my_weight = 85.5
my_height = 180
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'Black'

print("Let's talk aboyut %s %s." % (my_name, my_surname))
print("He is %4.2f cm tall" % my_weight)
print("He's got %s eyes and %d tall." % (my_eyes, my_height))
print("Testing the %s" % my_age)
#%%
# =============================================================================
# Exercise 6 - String and Text
# =============================================================================
x = "There are %i types of people." %10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print(x)
print(y)

print("I said: %r" % x)
print("I also said: '%s'." % y)

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print(joke_evaluation % hilarious)

w = "This is the left side of..."
e = "a string with a right side."
print(w + e)
#%%
# =============================================================================
# Exercise 7 - More Printing
# =============================================================================
print("Mary had a little lamb.")
print("Its fleece was white as %s." % 'snow')
print("And wverywhere that Mary went.")
print("."*10)

e1 = "C"
e2 = "h"
e3 = "e"
e4 = "e"
e5 = "s"
e6 = "e"
e7 = "B"
e8 = "u"
e9 = "r"
e10 = "g"
e11 = "e"
e12 = "r"
print(e1+e2+e3+e4+e5+e6,
      e7+e8+e9+e10+e11+e12)


#%%
# =============================================================================
# Exercise 8 - Printing Printing
# =============================================================================
formater = "%r %r %r %r"
print (formater % (1,2,3,4))
print(formater % ("one", "two", "three", "four"))
print(formater % (True, False, False, True))
print(formater % (formater, formater, formater, formater))
print(formater % (
        "I had this thing.",
        "That you could type up rigth.",
        "But it didn't sing.",
        "So I said goodnight."))
#%%
# =============================================================================
# Exercise 9 - Printing*3
# =============================================================================
days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFre\nMar\nApr\nMay\nJun\nJul\nAug"

print("Here are the days:", days)
print("Here are the months", months)

print("""
      There's something going on here.
      With the three double-quotes.
      We'll be abe to type as mus as we like
      Even 4 lines if we want, or 5, or 6
      """)
#%%
# =============================================================================
# Exercise 10 - What Was That
# =============================================================================
tabby_cat = "\tI'm tabbet in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
    \t* Cat food
    \t* Fishies
    \t* Catnip\n\t* Grass
"""
print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

#%%
# =============================================================================
# Exercise 11 - Asking Questions
# =============================================================================
print("How old are you?")
age = input()

print("How tall are you?")
height = input()

print("How much do you weigh")
weight = input()

print("So, you're %r old, %r tall and %r heavy." %(age, height, weight))
#%%
# =============================================================================
# Exercise 12 - Prompting People
# =============================================================================
age = input("How old are you? ")

print("So, you are %r" % age)
#%%
# =============================================================================
# Exercise  -
# =============================================================================

#%%
# =============================================================================
# Exercise  -
# =============================================================================

#%%
# =============================================================================
# Exercise  -
# =============================================================================

#%%
# =============================================================================
# Exercise  -
# =============================================================================

#%%
# =============================================================================
# Exercise  -
# =============================================================================


