#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    student = list(a_dictionary.keys())[0]
    score = a_dictionary[student]
    for i, v in a_dictionary.items():
        if score < v:
            student = i
            score = v
    return student
