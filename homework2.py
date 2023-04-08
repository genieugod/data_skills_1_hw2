# PPHA 30535
# Spring 2023
# Homework 2

# YOUR CANVAS NAME HERE
# YOUR GITHUB USER NAME HERE

# Due date: Sunday April 9th before midnight
# Write your answers in the space between the questions, and commit/push only 
# this file to your repo. Note that there can be a difference between giving a
# "minimally" right answer, and a really good answer, so it can pay to put 
# thought into your work.

#############

# Question 1: Write a function that takes two numbers as arguments, then
# sums them together.  If the sum is greater than 10, return the string 
# "big", if it is equal to 10, return "just right", and if it is less than
# 10, return "small".  Apply the function to each tuple of values in the 
# following list, with the end result being another list holding the strings 
# your function generates (e.g. ["big", "big", "small"]).

start_list = [(10, 0), (100, 4), (0, 0), (-15, -100), (5, 4)]

def sum_compare_to_10(number_1, number_2):
    sum = number_1 + number_2
    if (sum > 10):
        return "big"
    elif (sum < 10):
        return "small"
    else:
        return "just right"
result = []
for item in start_list:
    result.append(sum_compare_to_10(item[0], item[1]))
print(result)


# Question 2: The following code is fully-functional, but uses a global
# variable and a local variable.  Re-write it to work the same, but using an
# argument and a local variable.  Use no more than two lines of comments to
# explain why this new way is preferable to the old way.

# delete this line: a = 10
def my_func(a = 10):
    b = 30
    return a + b
x = my_func()

#new way is preferable since the local varaible is indenpendent won't be affected
#by other functions or affects other fucntions also the parameter can be changed while call the function


# Question 3: Write a function that can generate a random password from
# upper-case and lower-case letters, numbers, and special characters 
# (!@#$%^&*).  It should have an argument for password length, and should 
# check to make sure the length is between 8 and 16, or else warn the user 
# and exit.  Your function should also have a keyword argument named 
# "special_chars" that defaults to True.  If the function is called with the 
# keyword argument set to False instead, then the random values chosen should
# not include special characters.  Create a second similar keyword argument 
# for numbers. Use one of the two libraries below.
#import random
#from numpy import random

import random
def password_generator(length, special_chars = True, numbers = True):
    
    #check if password length within the range
    if length not in range(8, 17):
        return "length is not between 8 to 16"
    
    password_pool = []
    #adding A-Z ascii number to 
    password_pool.extend(range(65, 91))
    #adding a-z ascii number to 
    password_pool.extend(range(97, 123))
    
    
    if special_chars:
        #!@#$%^&*
        password_pool.extend([33,64,35,36,37,94,38,42])
        
    if numbers:
        #0-9
        password_pool.extend(range(48,58))
      
    password = ""
    for _ in range(length):
        password += chr(random.choice(password_pool))
        
    return password

#test_1
password_generator(15)

#test_2
password_generator(19)


# Question 4: Create a class that requires four arguments when an instance
# is created: one for the person's name, one for which COVID vaccine they
# have had, one for how many doses they've had, and one for whether they've
# ever had COVID.  Then create instances for four people:
#
# Aaron, Moderna, 3, False
# Ashu, Pfizer, 2, False
# Alison, none, 0, True
# Asma, Pfizer, 1, True
#
# Write two methods for this class, and one function:
# The first method named "get_record", which prints out a one-sentence summary
# of a specified person's records (e.g. Ashu has two doses of Phizer and...)
#
# The second method named "same_shot", which takes as an argument another person's
# record instance, and then prints whether or not the two people have the
# same kind of vaccine or not.
#
# A function named "all_data", which takes a container holding any number of these 
# instances and returns a simple list of all of their data 
# (e.g. [name, vaccine, doses, covid], [...])

# pip install module to translate digital number to word
# ref(https://www.geeksforgeeks.org/python-number-to-words-using-num2words/)
# pip install num2words

from num2words import num2words
class CovidRecord():
    def __init__(self, name, vaccine_brand, number_doses, had_covid):
        self.name = name
        self.vaccine_brand = vaccine_brand
        self.number_doses = number_doses
        self.had_covid = had_covid
        
    def get_record(self):
        number_words = num2words(self.number_doses)
        result = "%s has %s doses of %s " % (self.name, 
                                          number_words, 
                                          self.vaccine_brand)
        if self.had_covid:
            result += "and have had COVID."
        else:
            result += "and have never had COVID."
        return print(result)
        
    def same_shot(self, second_person):
        if (self.vaccine_brand == second_person.vaccine_brand):
            print("same kind of vaccine")
        else:
            print("not the same kind of vaccine")
    
        
        
        
record_Aaron = CovidRecord('Aaron', 'Moderna', 3, False)
record_Ashu = CovidRecord('Ashu', 'Pfizer', 2, False)
record_Alison = CovidRecord('Alison', None, 0, True)
record_Asma = CovidRecord('Asma', 'Pfizer', 1, True)

record_Aaron.get_record()

def all_data(covid_record):
    all_record_list = []
    for instance in covid_record:
        individual = []
        individual.extend([instance.name,
                          instance.vaccine_brand,
                          instance.number_doses,
                          instance.had_covid])
        all_record_list.append(individual)
        
    return all_record_list
        

covid_record = [record_Aaron, record_Ashu, record_Alison, record_Asma]

all_data(covid_record)


















