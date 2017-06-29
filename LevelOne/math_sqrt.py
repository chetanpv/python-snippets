# Question:
# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.
# Example
# Let us assume the following comma separated input sequence is given to the program:
# 100,150,180
# The output of the program should be:
# 18,22,24

import math
print "\nEnter a number(s): "
values = raw_input()
arr = values.split(",")
output = []
for i in arr:
    output.append(str(int(round(math.sqrt((2*50*int(i))/30)))))
print ','.join(output)
