#!/usr/bin/python3
def roman_to_int(roman_string):
    total = 0
    prev_value = 0
    roman_dictionary = {
         'M': 1000,
         'D': 500,
         'C': 100,
         'L': 50,
         'X': 10,
         'V': 5,
         'I': 1
         }
    if not isinstance(roman_string, str):
        return total
    for letter in roman_string:
        value = roman_dictionary.get(letter, 0)
        if value == 0:
            return 0
        if 0 < prev_value < value:
            total += value - prev_value*2
        else:
            prev_value = value
            total += value
    return total
