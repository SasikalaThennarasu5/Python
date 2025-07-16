emails = ["a@x.com", "b@x.com", "a@x.com", "c@x.com"]
unique_emails = set(emails)
cleaned_list = list(unique_emails)
print("Cleaned emails:", cleaned_list)
print("Is 'b@x.com' present?", "b@x.com" in unique_emails)