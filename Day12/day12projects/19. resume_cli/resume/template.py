def generate_text(resume):
    lines = [
        f"{resume['name']}",
        f"Email: {resume['email']} | Phone: {resume['phone']}",
        "-" * 40,
        "Summary:",
        resume['summary'],
        "\nExperience:",
        "\n".join(f"- {job.strip()}" for job in resume['experience']),
        "\nEducation:",
        resume['education'],
        "\nSkills:",
        ", ".join(skill.strip() for skill in resume['skills']),
    ]
    return "\n".join(lines)

def generate_markdown(resume):
    lines = [
        f"# {resume['name']}",
        f"**Email:** {resume['email']} | **Phone:** {resume['phone']}",
        "---",
        "## Summary",
        resume['summary'],
        "## Experience",
        "\n".join(f"- {job.strip()}" for job in resume['experience']),
        "## Education",
        resume['education'],
        "## Skills",
        ", ".join(skill.strip() for skill in resume['skills']),
    ]
    return "\n\n".join(lines)