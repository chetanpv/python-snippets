# Question:
# Use a list comprehension to square each odd number in a list. The list is input by a sequence
# of comma-separated numbers.
# Suppose the following input is supplied to the program:
# 1,2,3,4,5,6,7,8,9
# Then, the output should be:
# 1,3,5,7,9

print "\nEnter sequence of numbers: "
numbers = raw_input().split(",")
output = []
for i in numbers:
    n = int(i)
    if n % 2 != 0:
        output.append(str(n*n))
print ",".join(output)

output = [str(int(i)*int(i)) for i in numbers if int(i) % 2 != 0]
print ",".join(output)
