a = "chetanisagoodboychetanischetan"
b = "chetan"


al = list(a)
blen = len(b)

count = 0

for i in range(len(a)):
    if a[i] == b[0]:
        substring = a[i:i+blen]
        if substring == b:
            count += 1
print count
