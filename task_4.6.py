# Task 4.6: Challenge – Activity Selection Problem
# ----------------------------------------------
# This is a classic greedy scheduling problem.
#
# Problem:
# You are given n activities with start and finish times.
# Select the maximum number of activities that can be performed by one person,
# assuming that a person can only work on a single activity at a time.
#
# Input:
# - List of activities with (start_time, finish_time)
#
# Output:
# - Maximum number of non-overlapping activities that can be performed.
#
# Example:
# Activities = [(1,2), (3,4), (0,6), (5,7), (8,9), (5,9)]
# Output: 4 activities (choose: (1,2), (3,4), (5,7), (8,9))
#
# Hint: Sort activities by finish time, then pick the next compatible activity.
#
# This is your challenge task for the nerds!

def activity_selection(activities):
    activities_with_index = [(start, finish, i) for i, (start, finish) in enumerate(activities)]
    activities_with_index.sort(key=lambda x: x[1])
    
    selected = []
    last_finish_time = -1
    
    for start, finish, original_index in activities_with_index:
        if start >= last_finish_time:
            selected.append((start, finish, original_index))
            last_finish_time = finish
    
    return len(selected), selected

def print_activity_selection_solution(activities, num_selected, selected_activities):
    print("Original Activities: (start, finish)")
    for i, (start, finish) in enumerate(activities):
        print(f"  Activity {i}: ({start}, {finish})")
    
    print(f"\nMaximum number of non-overlapping activities: {num_selected}")
    print("Selected activities:")
    
    selected_activities.sort(key=lambda x: x[0])
    
    for start, finish, original_index in selected_activities:
        print(f"  Activity {original_index}: ({start}, {finish})")
    
    print("\nTimeline visualization:")
    timeline = ""
    max_time = max(finish for start, finish in activities) + 1
    
    for t in range(max_time):
        timeline += f"{t:2d} "
    print("Time: " + timeline)
    
    for start, finish, original_index in selected_activities:
        visual = "   " * start + "██" * (finish - start) + "   " * (max_time - finish)
        print(f"Act {original_index}: {visual}")

activities1 = [(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]
num_selected1, selected1 = activity_selection(activities1)
print_activity_selection_solution(activities1, num_selected1, selected1)

print("\n" + "="*60)

activities2 = [(1, 4), (3, 5), (0, 3), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)]
num_selected2, selected2 = activity_selection(activities2)
print_activity_selection_solution(activities2, num_selected2, selected2)
