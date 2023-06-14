def common_elements(set_1, set_2):
    # Create an empty set to store the common elements
    common = set()

    # Iterate over each element in set_1
    for element in set_1:
        # Check if the element is also in set_2
        if element in set_2:
            # Add the element to the common set
            common.add(element)

    return common

