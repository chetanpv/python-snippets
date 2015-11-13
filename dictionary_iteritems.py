data = {'cpu' :{'cpu.total_logical_cores': 3L, 'cpu.used_mhz': 2600L, 'cpu.total_mhz': 2600L, 'cpu.used_perc': 16L}, 'mem': {'mem.used_mb': 2455L, 'mem.used_perc': 14.985045473966919, 'mem.total_mb': 16383L}}

all_iter = data.iteritems()

for i in all_iter:
    # Iterate for all the values of the outer dictionary
    A = i[1].iteritems()
    for a in A:
        print "--------------"
        print a
        print "--------------"

