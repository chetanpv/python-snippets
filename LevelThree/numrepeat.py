arr = [1,1,2,2,3,3,3,4,4,5]

rep = []
count = 1

for i in range(0, len(arr)):
    if i == len(arr)-1:
        rep.append(count)
    elif arr[i] == arr[i+1]:
        count += 1
    else:
        rep.append(count)
        count = 1

print rep