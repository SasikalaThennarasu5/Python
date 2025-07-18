# main.py

from feedback_handler import store_feedback

# Initialize feedback dictionary
feedback_db = {}

# Collecting feedback
store_feedback(feedback_db, 101, "The product is very useful and reliable.")
store_feedback(feedback_db, 102, "I find the service fast and reliable.")

# Display stored feedback
for customer_id, data in feedback_db.items():
    print(f"Customer ID: {customer_id[0]}")
    print(f"Feedback: {data['feedback']}")
    print(f"Keywords: {data['keywords']}")
    print("-" * 40)