# Question:
# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3

print "\nEnter sentence: "
sent = raw_input()
digit = 0
letters = 0

for i in sent:
    if i.isdigit():
        digit += 1
    elif i.isalnum():
        letters += 1

print "DIGITS: ", digit
print "LETTERS: ", letters
