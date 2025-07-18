# poll_utils.py

def cast_vote(voters_set, poll_results, voter_id, choice):
    """Record a vote if the voter hasn't already voted."""
    voter_key = (voter_id,)  # Using tuple for voter ID

    if voter_key in voters_set:
        print(f"Voter {voter_id} has already voted.")
        return False

    voters_set.add(voter_key)

    if choice in poll_results:
        poll_results[choice] += 1
    else:
        poll_results[choice] = 1

    print(f"Voter {voter_id} successfully voted for {choice}.")
    return True


def show_results(poll_results):
    """Display the poll results."""
    print("\nPoll Results:")
    for choice, count in poll_results.items():
        print(f"{choice}: {count} votes")
    print("-" * 40)
