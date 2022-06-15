#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return None
    for key, value in a_dictionary.items():
        biggest_value = max(a_dictionary.value())
        if value is biggest_value:
            return key


