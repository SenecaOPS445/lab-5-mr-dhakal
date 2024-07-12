#!/usr/bin/env python3
# Author ID: mrdhakal

import os


def read_file_string(file_name):
    # Takes file_name as string for a file name, returns its entire contents as a string
    
    f = open('data.txt', 'r')
    text = f.read()
    f.close()
    
    return text


def read_file_list(file_name):
    # Takes a file_name as string for a file name, 

    f = open('data.txt', 'r')
    li = f.readlines()
    f.close()

    result = []
    for line in li:
        if line[-1] == '\n':
            result.append(line[:-1])
        else:
            result.append(line)
    
    
    # return its entire contents as a list of lines without new-line characters
    return result


def append_file_string(file_name, string_of_lines):
    # Takes two strings, appends the string to the end of the file

    f = open('data.txt', 'a')
    append = f.write(string_of_lines)
    f.close()
    return append


def write_file_list(file_name, list_of_lines):
    # Takes a string and list, writes all items from list to file where each item is one line

    f = open('data.txt', 'w')
    for line in list_of_lines:
        write = f.write(line + '\n')
    
    f.close()

    return write

def copy_file_add_line_numbers(file_name_read, file_name_write):
    # Takes two strings, reads data from first file, writes data to new file, adds line number to new file
    
    r = open('data.txt', 'r') 
    li = r.readlines()
    r.close()
    w = open('newfile.txt', 'w') 
    line_number = 1
    for line in li:
        write = w.write(f"{line_number}:{line}")
        line_number +=1
        return write
    
    
    w.close()
    
if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']
    append_file_string(file1, string1)
    print(read_file_string(file1))
    write_file_list(file2, list1)
    print(read_file_string(file2))
    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))
