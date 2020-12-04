# Advent of code 2020
# Day 1
# Report Repair
#
# Find the two numbers from the input array that sum to 2020.
# What's the value of those two numbers multiplied?

input = [1721, 979, 366, 299, 675, 1456]

# Naive algorithm: check each pair (done)
# Improvement: a + b will be the same as b + a, so we can reject half of the pairs to check: when we're evaluating a new value to pair with in the table, just start with the index of that value and only go forward, the previous indexes have been checked already (done)
# Improvement: if both numbers 3-digit long, reject pair (done)
# Improvement: if both pairs 4-digit long and > 1020, reject pair (done)

# 1. Naive solution:

def naive_solution_O_n2(input):
    input_len = len(input)

    for i in range(input_len):
        for j in range(input_len):
            i_len = len(str(input[i]))
            j_len = len(str(input[j]))

            if i_len == 3 and j_len == 3:
                continue

            if i_len == 4 and j_len == 4:
                if input[i] > 1020 and input[j] > 1020:
                    print i, j
            if input[i] + input[j] == 2020:
                print 'found i + j that sums to 2020: i=' + str(i) + ', j=' + str(j) + ' (' + str(input[i]) + ',' + str(input[j]) + ')'
                return

naive_solution_O_n2(input)

# Next: read input from the file, so I can type in the answer in web UI

# Next: read on algorithms on how to do it in a smart way (algorithm to find a pair of values)

