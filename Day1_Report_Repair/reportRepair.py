# Advent of code 2020
# Day 1
# Report Repair
#
# Find the two numbers from the input array that sum to 2020.
# What's the value of those two numbers multiplied?

DEFAULT_INPUT = [1721, 979, 366, 299, 675, 1456]

# Naive algorithm: check each pair (done)
# Improvement: a + b will be the same as b + a, so we can reject half of the pairs to check: when we're evaluating a new value to pair with in the table, just start with the index of that value and only go forward, the previous indexes have been checked already (done)
# Improvement: if both numbers 3-digit long, reject pair (done)
# Improvement: if both pairs 4-digit long and > 1020, reject pair (done)

# 1. Naive solution:

def naive_solution_O_n2(input):
    input_len = len(input)
    attempts_counter = 0

    for i in range(input_len):
        for j in range(input_len):
            attempts_counter += 1

            i_len = len(str(input[i]))
            j_len = len(str(input[j]))

            if i_len == 3 and j_len == 3:
                # a sum of 3-digit values will never equal to 2020
                continue

            if i_len == 4 and j_len == 4:
                if input[i] > 1020 and input[j] > 1020:
                    # a sum will always be > 2020
                    continue

            input_i = input[i]
            input_j = input[j]

            print "attempt " + str(attempts_counter) + ": " + str(input_i), str(input_j), "sum: " + str(input_i + input_j)

            if input_i + input_j == 2020:
                print 'found i + j that sums to 2020: i=' + str(i) + ', j=' + str(j) + ' (' + str(input_i) + ',' + str(input_j) + ')'
                return

from common import read_input_from_stdin

input = read_input_from_stdin()
naive_solution_O_n2(input)

# Next: read on algorithms on how to do it in a smart way (algorithm to find a pair of values)

