#!/isr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if len(my_list) == 0:
        return
    last_element = my_list[-1]
    print("{:d}".format(last_element))
    print_reversed_list_integer(my_list[:-1])
