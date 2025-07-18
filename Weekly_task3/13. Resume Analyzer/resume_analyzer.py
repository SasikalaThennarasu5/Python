# resume_analyzer.py

def extract_skills(resume_text):
    """Extract unique skills from resume text using a set."""
    words = set(resume_text.lower().split())
    # Example list of known skill-related keywords
    skill_keywords = {'python', 'java', 'sql', 'excel', 'communication', 'leadership', 'teamwork'}
    return words & skill_keywords


def store_resume_skills(database, applicant_id, resume_text):
    """Store applicant skills using tuple ID and dictionary."""
    applicant_key = (applicant_id,)
    skills = extract_skills(resume_text)
    database[applicant_key] = {
        'skills': skills
    }
    print(f"Stored skills for applicant ID {applicant_id}")


def show_all_applicants(database):
    """Display all stored applicants and their skills."""
    print("\nResume Analysis:")
    for applicant_key, data in database.items():
        print(f"Applicant ID: {applicant_key[0]}")
        print(f"Skills: {data['skills']}")
        print("-" * 40)
