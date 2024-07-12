#!/usr/bin/env python3
# Author ID: [seneca_id]

def add(number1, number2):
    # Add two numbers together, return the result, if error return string 'error: could not add numbers'
    try:
        add_num = int(number1) + int(number2)
        return add_num
    except Exception as e:
        return e



def read_file(filename):
    # Read a file, return a list of all lines, if error return string 'error: could not read file'

    try:
        file = open(filename, 'r')
        lines = file.readlines()
        return lines
    except Exception as e:
        return e


if __name__ == '__main__':
    print(add(10,5))                        # works
    print(add('10',5))                      # works
    print(add('abc',5))                     # exception
    print(read_file('seneca2.txt'))         # works
    print(read_file('file10000.txt'))       # exception