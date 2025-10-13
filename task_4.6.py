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
	"""Return the maximum number of non-overlapping activities and the selected activities."""
	# Sort activities by finish time
	activities = sorted(activities, key=lambda x: x[1])
	selected = []
	last_finish = -float('inf')
	for start, finish in activities:
		if start >= last_finish:
			selected.append((start, finish))
			last_finish = finish
	return len(selected), selected

if __name__ == "__main__":
	n = int(input("Enter number of activities: "))
	activities = []
	for i in range(n):
		start = int(input(f"Enter start time of activity {i+1}: "))
		finish = int(input(f"Enter finish time of activity {i+1}: "))
		activities.append((start, finish))
	max_count, selected_acts = activity_selection(activities)
	print(f"Maximum number of non-overlapping activities: {max_count}")
	print(f"Selected activities: {selected_acts}")
