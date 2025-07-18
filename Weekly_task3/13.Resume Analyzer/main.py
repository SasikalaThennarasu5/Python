# main.py

from resume_analyzer import store_resume_skills, show_all_applicants

# Initialize database for storing resumes
database = {}

# Analyze resumes
store_resume_skills(database, 401, "Python Java SQL teamwork communication")
store_resume_skills(database, 402, "Excel Leadership Communication Python")

# Display all analyzed results
show_all_applicants(database)
