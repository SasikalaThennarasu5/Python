class AlreadyVotedError(Exception): pass

def vote_system(voted):
    try:
        name = input("Name: ")
        if name in voted:
            raise AlreadyVotedError("Already voted")
        voted.add(name)
    except Exception as e:
        print(e)
    finally:
        print("Thanks for participating")