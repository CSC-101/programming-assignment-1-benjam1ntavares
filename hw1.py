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
# the add_prices function will take two parameters, each of type price, and it will return the sum of the input prices
# s.t. cents never goes above 99

def add_prices(price1:data.Price, price2:data.Price) -> data.Price:
    dollars = price1.dollars + price2.dollars
    cents = price1.cents + price2.cents
    if cents > 99:
        dollars = dollars + cents // 100
        cents = cents % 100
        return data.Price(dollars,cents)
    else:
        return data.Price(dollars,cents)

# Part 5
#######################################################################################################################
# function rectangle_area will have one parameter, rectangle (as the class is defined in data.py) and it will return the
# area of the rectangle (assuming that the rectangle is properly aligned with the x-y plane.

def rectangle_area(rect: data.Rectangle) -> float:
    y_height = rect.top_left.y - rect.bottom_right.y
    x_width = rect.top_left.x - rect.bottom_right.x
    return abs(y_height) * abs(x_width)

# Part 6
#######################################################################################################################
# books by author will take two parameters, one of type str, and one of type list[Book], where book is a class defined
# in data.py. the books_by_author function will find all of the books written by the same author

def books_by_author(author:str, books:list[data.Book]) -> list[data.Book]:
    sorted_books = []
    for i in books:
        if author in i.authors:
            sorted_books.append(i)
    return sorted_books



    # Part 7


# Part 8


