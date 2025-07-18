# feedback_handler.py

def extract_keywords(feedback):
    """Extract unique keywords from feedback using set."""
    words = feedback.lower().split()
    # Example filter: exclude common words
    common_words = {'the', 'is', 'and', 'a', 'of', 'to', 'in'}
    keywords = set(words) - common_words
    return keywords


def store_feedback(feedback_db, customer_id, feedback):
    """Store feedback in the dictionary with customer ID as tuple."""
    customer_key = (customer_id,)  # tuple with customer ID
    feedback_db[customer_key] = {
        'feedback': feedback,
        'keywords': extract_keywords(feedback)
    }