"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    for item in items:
        if item in frequencies:
            count = frequencies[item]
            frequencies.update({item: count + 1})
        else:
            frequencies[item] = 1

    return frequencies

print(frequencies(['a', 'a', 'b', 'b', 'b', 'c']))