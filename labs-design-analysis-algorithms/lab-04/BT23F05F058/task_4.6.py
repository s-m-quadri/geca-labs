def activity_selection(activities):
    """
    activities: list of tuples (start_time, finish_time)
    returns: list of selected activities with maximum count
    """
    # Step 1: Sort activities by finish time
    activities.sort(key=lambda x: x[1])

    selected = []
    last_finish_time = -1

    # Step 2: Pick activities greedily
    for start, finish in activities:
        if start >= last_finish_time:
            selected.append((start, finish))
            last_finish_time = finish

    return selected


# Example usage
activities = [(1,2), (3,4), (0,6), (5,7), (8,9), (5,9)]
selected_activities = activity_selection(activities)
print(f"Maximum number of activities: {len(selected_activities)}")
print(f"Selected activities: {selected_activities}")
# Output:
# Maximum number of activities: 4
# Selected activities: [(1,2), (3,4), (5,7), (8,9)]
