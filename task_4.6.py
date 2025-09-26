def activity_selection(activities):
    activities.sort(key=lambda x: x[1])
    selected = []
    last_finish = -1
    for start, finish in activities:
        if start >= last_finish:
            selected.append((start, finish))
            last_finish = finish
    return selected

activities = [(1,2), (3,4), (0,6), (5,7), (8,9), (5,9)]
selected = activity_selection(activities)
print("Maximum number of activities:", len(selected))
print("Selected activities:", selected)
