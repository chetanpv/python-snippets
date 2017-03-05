word = "My name is chetan"
f = {}
max_key = None
max_value = 0
for i in word:
    if f.has_key(i):
        f[i] = f[i] + 1
    else:
        f[i] = 1
    if f[i] > max_value:
        max_value = f[i]
        max_key = i
print f
print max_key
print max_value
