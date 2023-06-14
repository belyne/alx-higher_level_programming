#!/usr/bin/python3
def uniq_add(my_list=[]):
    # Create an empty set to store unique integers
    unique_integers = set()
    # Initialize the sum to 0
    total_sum = 0

    # Iterate over each element in the list
    for element in my_list:
        # Check if the element is not already in the set
        if element not in unique_integers:
            # Add the element to the set
            unique_integers.add(element)
            # Add the element to the total sum
            total_sum += element

    return total_sum
