# Define a class with a generator which can iterate the numbers, which are divisible by 7,
# between a given range 0 and n.

import time


def yrange(n):
    i = 1
    while i < n:
        if i % 7 == 0:
            yield i
        i += 1

y = yrange(50)

try:
    # Observe no next(). Instead its next
    some = y.next
    while some:
        print y.next()
except StopIteration:
    print "sdf"

