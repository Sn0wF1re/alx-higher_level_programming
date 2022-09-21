#!/usr/bin/python3
def remove_char_at(str, n):
    newString = ""
    i = 0
    for letter in str:
        if i != n:
            newString += letter
        i += 1
    return (newString)
