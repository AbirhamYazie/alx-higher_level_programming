#!/usr/bin/python3
def best_score(a_dictionary):
    biggest_value = max(a_dictionary.value())
    for key, value in a_dictionary.items():
        if a_dictionary is None or a_dictionary == {}:
            return None
        else:
            value is biggest_value
            return key
