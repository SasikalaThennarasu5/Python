responses = {"r1", "r2", "r3"}
new_responses = {"r4", "r5"}
responses.update(new_responses)

removed = set()
responses.discard("r1")
removed.add("r1")

try:
    responses.remove("invalid")
except KeyError:
    print("Invalid response skipped")

print("Remaining:", responses)
print("Removed:", removed)
print("Popped:", responses.pop())