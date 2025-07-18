# exam_creator.py

def add_question(exam_db, question_id, question_text, topics_set, topic):
    """Add a question with unique ID and manage unique topics."""
    question_key = (question_id,)  # Tuple for question ID
    topics_set.add(topic)  # Track unique topics
    
    exam_db[question_key] = {
        'question': question_text,
        'topic': topic
    }
    print(f"Added Question ID {question_id}: '{question_text}' under topic '{topic}'.")


def show_all_questions(exam_db):
    """Display all questions in the exam."""
    print("\nExam Questions:")
    for question_key, data in exam_db.items():
        print(f"Question ID: {question_key[0]}, Topic: {data['topic']}")
        print(f"Q: {data['question']}")
    print("-" * 40)


def show_all_topics(topics_set):
    """Display all unique topics."""
    print(f"\nAvailable Topics: {topics_set}")
    print("-" * 40)
