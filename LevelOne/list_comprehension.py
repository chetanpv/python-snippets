a = []
for i in xrange(1,10):
    if i % 2 == 0:
        a.append(i)
print a

print [i for i in xrange(1,10) if i%2==0]
# [listappend for_loop condition]
