def activity_selection(activities):
    """
    activities: list of tuples (start_time, finish_time)
    Returns: list of selected activities
    """
    # Sort activities by finish time
    activities.sort(key=lambda x: x[1])
    
    selected_activities = []
    last_finish_time = -1  # Initialize with a time before all activities
    
    for activity in activities:
        start, finish = activity
        if start >= last_finish_time:
            selected_activities.append(activity)
            last_finish_time = finish
    
    return selected_activities

# Test the function
n = int(input("Enter number of activities: "))
activities = []
for i in range(n):
    s = int(input(f"Enter start time of activity {i+1}: "))
    f = int(input(f"Enter finish time of activity {i+1}: "))
    activities.append((s, f))

selected = activity_selection(activities)
print(f"Maximum number of activities: {len(selected)}")
print(f"Selected activities: {selected}")
