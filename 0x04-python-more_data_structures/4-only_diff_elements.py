#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    # Create an empty set to store the elements present in only one set
    diff_elements = set()

    # Iterate over each element in set_1
    for element in set_1:
        # Check if the element is not in set_2
        if element not in set_2:
            # Add the element to the diff_elements set
            diff_elements.add(element)

    # Iterate over each element in set_2
    for element in set_2:
        # Check if the element is not in set_1
        if element not in set_1:
            # Add the element to the diff_elements set
            diff_elements.add(element)

    return diff_elements
