import data

# Write your functions for each part in the space below.


# Part 1
######################################################################################################################
# The vowel_count function will have a parameter of type string, and it will return the number of vowels in the
# given string using the built-in string function to separate the characters, and a for loop to iterate through each
# character and check if it is a vowel

def vowel_count(input_string:str) -> int:
    listed_characters = list(input_string)
    vowels = ['a', 'e', 'i', 'o', 'u','A','E','I','O','U']
    v_count = 0
    for i in listed_characters:
        if i in vowels:
            v_count += 1
    return v_count


# Part 2
######################################################################################################################
# The short_lists function takes a list of lists of integers and returns a new list of all of the nested lists that are
# of the length 2

def short_lists(input_list:list[list[int]]) -> list:
    output_list = []
    for i in input_list:
        if len(i) ==  2:
            output_list.append(i)
    return output_list


# Part 3
########################################################################################################################
# ascending_pairs function will take a list of lists, identify all "short lists" (lists of length 2) and it will sort
# the "short lists" into ascending order

def ascending_pairs(input_list:list[list[int]]) -> list[list[int]]:
    output_list = []
    for i in input_list:
        if len(i) == 2:
            output_list.append(sorted(i))
        else:
            output_list.append(i)
    return output_list


# Part 4
########################################################################################################################
#
#
#
# #

# Part 5


# Part 6


# Part 7


# Part 8


