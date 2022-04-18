"""
Created by hu-jinwen on 2022/4/4
"""

def print_line(char, times):

    print(char * times)

def print_lines (x, y):
    """
    getting more split lines
    :param x: copy words
    :param y: times
    """
    row = 0
    while row < 5:
        print_line(x, y)
        row += 1

print_lines("%", 10)




