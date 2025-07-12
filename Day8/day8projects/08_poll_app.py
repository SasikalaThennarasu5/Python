# Simple Poll App

responses = ["Yes", "No", "Yes", "Maybe", "Yes", "No", "yes"]

# Normalize and remove invalid
responses = [resp.capitalize() for resp in responses if resp.capitalize() in ["Yes", "No"]]

yes_count = responses.count("Yes")
no_count = responses.count("No")

print(f"Yes: {yes_count}, No: {no_count}")
