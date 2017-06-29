a = [9, 9, 46, 76, 84, 114, 122, 150, 151, 152, 155, 198, 199]
T=1

def make_zero(arr, T):
    index_values = []
    for i in range(0, len(arr)):
        if i == 0:
            if abs(arr[i] - arr[i+1]) < 2*T:
                index_values.append(i)
        elif i == len(arr):
            if abs(arr[i] - arr[i-1]) < 2*T:
                index_values.append(i)
        elif abs(arr[i] - arr[i-1]) < 2*T:
            index_values.append(i)
        elif abs(arr[i] - arr[i+1]) < 2*T:
            index_values.append(i)
    for j in index_values:
        arr[j] = 0
    return arr

output = make_zero(a,T)
print output