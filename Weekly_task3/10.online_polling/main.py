# main.py

from poll_utils import cast_vote, show_results

# Initialize data structures
voters_set = set()
poll_results = {}

# Simulate voting
cast_vote(voters_set, poll_results, 201, "Option A")
cast_vote(voters_set, poll_results, 202, "Option B")
cast_vote(voters_set, poll_results, 203, "Option A")
cast_vote(voters_set, poll_results, 201, "Option B")  # Duplicate voter ID

# Display final poll results
show_results(poll_results)
