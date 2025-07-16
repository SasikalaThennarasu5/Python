# 13. Resume Skill Matcher

resumes = {
    "R1": {"skills": ["Python", "SQL"], "experience": 2},
    "R2": {"skills": ["JavaScript", "HTML"], "experience": 4},
}

# Search by skill
required = "Python"
matched = [rid for rid, data in resumes.items() if required in data["skills"]]
print("Matched Resumes:", matched)

# Filter by experience
exp_filtered = {k: v for k, v in resumes.items() if 2 <= v["experience"] <= 4}
print("Experience Filtered:", exp_filtered)
