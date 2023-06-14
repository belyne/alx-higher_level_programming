#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    # Update the value if the key already exists in the dictionary
    if key in a_dictionary:
        a_dictionary[key] = value
    else:
        # Add the key/value pair to the dictionary if the key doesn't exist
        a_dictionary[key] = value

    return a_dictionary
