# Write a program that computes the net amount of a bank account based on a transaction log from console input.
# The transaction log format is shown as following:
# D 100
# W 200
# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:
# D 300
# D 300
# W 200
# D 100
# Then, the output should be:
# 500

total = 0
while True:
    statement = raw_input()
    if not statement:
        break
    mtype, amount = statement.split(" ")
    if not (mtype or amount):
        break
    if mtype == "D":
        total += int(amount)
    elif mtype == "W":
        total -= int(amount)

print total
