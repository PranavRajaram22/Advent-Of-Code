#Group by value

def group_by_value(iterable):
    groups = []
    currgroup = [iterable[0]]
    for num in iterable[1:]:
        if num != currgroup[-1]:
            groups.append(currgroup.copy())
            currgroup = []
        currgroup.append(num)

    groups.append(currgroup.copy())

    return groups

def group_list_by_empty_line(iterable):
    groups = []
    currgroup = []
    for element in iterable:
        if element != '':
            currgroup.append(element)
        else:
            groups.append(currgroup.copy())
            currgroup = []
    groups.append(currgroup)
    return groups




