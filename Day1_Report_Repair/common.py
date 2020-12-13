# Advent of Code 2020
# common.py

def read_input_from_stdin():
    import sys
    input = []
    for line in sys.stdin:
        input.append(int(line))
    return input
