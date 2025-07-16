email_content = "Subject: #Urgent #Meeting #Important"
tags = {word[1:] for word in email_content.split() if word.startswith("#")}
print("Tags:", ", ".join(tags))