# main.py

from exam_creator import add_question, show_all_questions, show_all_topics

# Initialize data structures
exam_db = {}
topics_set = set()

# Add questions
add_question(exam_db, 801, "What is the capital of France?", topics_set, "Geography")
add_question(exam_db, 802, "Explain OOP concepts in Python.", topics_set, "Programming")
add_question(exam_db, 803, "Describe the water cycle.", topics_set, "Science")
add_question(exam_db, 804, "Name three renewable energy sources.", topics_set, "Science")  # Duplicate topic

# Display exam and topics
show_all_questions(exam_db)
show_all_topics(topics_set)
