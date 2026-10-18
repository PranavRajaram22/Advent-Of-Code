with open('2015 input') as file:
    stats = [line.strip() for line in file]

for i, stat in enumerate(stats):
    stat = stat.split(" ")
    stat.pop(1)
    stat.pop(1)
    stat.pop(2)
    stat.pop(2)
    for x in range(6):
        stat.pop(3)
    stat.pop(-1)
    stat[1] = int(stat[1])
    stat[2] = int(stat[2])
    stat[3] = int(stat[3])
    stat[0] = i
    #name as index, speed, time, rest time
    stats[i] = stat

race_time = 2503 #change to 2503

distances = []

for stat in stats:
    time_for_fly_and_rest = stat[2] + stat[3]
    remaining = race_time % time_for_fly_and_rest
    num_cycles = race_time // time_for_fly_and_rest
    distance = 0
    if remaining >= stat[2]:
        distance += stat[1] * stat[2]
    else:
        distance += stat[1] * (stat[2] - remaining)

    distance += num_cycles * stat[1] * stat[2]

    distances.append(distance)

print(f"Part 1: {max(distances)}")

points = [0] * len(stats)
distances = [0] * len(stats)
for second in range(race_time):
    for stat in stats:
        if second % (stat[2] + stat[3]) < stat[2]:
            distances[stat[0]] += stat[1]

    for i, distance in enumerate(distances):
        if distance == max(distances):
            points[i] += 1


print(f"Part 2: {max(points)}")




