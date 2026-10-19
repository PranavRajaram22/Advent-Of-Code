from collections import defaultdict, Counter

with open('2018 input') as file:
    logs = [line.strip() for line in file]

logs = sorted(logs)

times = defaultdict(list)

time = 0
currguard = None
for log in logs:
    log = log.split(" ")
    log[1] = log[1][:-1]

    if log[1].startswith('23'):
        currtime = 0
    else:
        currtime = int(log[1].split(":")[1])


    if 'Guard' in log:
        guard = int(log[3][1:])
        currguard = guard
    else:
        if "wakes" in log:
            for t in range(time, currtime):
                times[currguard].append(t)
        elif "asleep" in log:
            time = currtime


maxtime = 0

for intervals in times.values():
    maxtime = max(maxtime, len(intervals))


for guard in times.keys():
    if len(times[guard]) == maxtime:
        maxguard = guard



timeintervals = times[maxguard]
c = Counter(timeintervals)

maxocc = max(c.values())
for t in c.keys():
    if c[t] == maxocc:
        print(f"Part 1: {t*maxguard}")

maxmins = dict()
for guard in times.keys():
    maxmins[guard] = max(set(times[guard]), key=times[guard].count)


finalocc = 0
maxguard = None
maxtime = 0
for guard in maxmins.keys():
    time = maxmins[guard]
    occ = times[guard].count(time)
    if occ > finalocc:
        finalocc = occ
        maxguard = guard
        maxtime = time

print(f"Part 2: {maxguard*maxtime}")


