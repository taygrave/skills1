# Things you should be able to do.

number_list = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
word_list = [ "What", "about", "the", "Spam", "sausage", "spam", "spam", "bacon", "spam", "tomato", "and", "spam"]

# Write a function that takes a list of numbers and returns a new list with only the odd numbers.
def all_odd(number_list):
    new_list = []
    for number in number_list:
        if number % 2 != 0:
            new_list.append(number)
    print "List of only odd numbers:", new_list
    return new_list

all_odd(number_list)

# Write a function that takes a list of numbers and returns a new list with only the even numbers.
def all_even(number_list):
    new_list = []
    for number in number_list:
        if number % 2 == 0:
            new_list.append(number)
    print "List of only even numbers:", new_list
    return new_list

all_even(number_list)

# Write a function that takes a list of strings and (creates?) a new list with all strings of length 4 or greater.
def long_words(word_list):
    new_list = []
    index = 0
    for word in word_list:
        if len(word_list[index]) >= 4:
            new_list.append(word)
        index += 1
    print "List of words with 4 or more characters:", new_list
    return new_list

long_words(word_list)

# Write a function that finds the smallest element in a list of integers and returns it.
def smallest(number_list):
    new_list = sorted(number_list)
    print new_list[0]
    return new_list[0]

smallest(number_list)

# Write a function that finds the largest element in a list of integers and returns it.
def largest(number_list):
    return None

# Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
def halvesies(number_list):
    return []

# Write a function that takes a list of words and returns a list of all the lengths of those words.
def word_lengths(word_list):
    return []

# Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(number_list):
    return 0

# Write a function that multiplies all the numbers in a list together.
def mult_numbers(number_list):
    return 0

# Write a function that joins all the strings in a list together (without using the join method) and returns a single string.
def join_strings(word_list):
    return ""

# Write a function that takes a list of integers and returns the average (without using the avg method)
def average(number_list):
    return 0