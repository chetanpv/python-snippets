# Question:
# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106

sum = 0
a = []
print "\n Enter a number, How many times should it go on: "
number, times = raw_input().split(",")

for i in xrange(1, int(times)+1):
    sum += int(number*i)
print sum
