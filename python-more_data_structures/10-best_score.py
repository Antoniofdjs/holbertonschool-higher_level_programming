#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        top_score = max(a_dictionary, key=a_dictionary.get)
        return top_score
    return None
