#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # Create a new list to store the replaced elements
    new_list = []
    for element in my_list:
        # Check if the element matches the search element
        if element == search:
            # Replace the element with the new element
            new_list.append(replace)
        else:
            # Keep the element as it is
            new_list.append(element)

    return new_list
