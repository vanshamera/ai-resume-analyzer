import re

skills_db = ["python", "java", "sql", "machine learning", "data analysis", "excel"]

def extract_skills(text):
    found = []
    for skill in skills_db:
        if re.search(skill, text.lower()):
            found.append(skill)
    return found

def suggest_improvements(found_skills):
    suggestions = []
    if "python" not in found_skills:
        suggestions.append("Consider learning Python")
    if "machine learning" not in found_skills:
        suggestions.append("Add Machine Learning basics")
    if "sql" not in found_skills:
        suggestions.append("Learn SQL for data handling")
    return suggestions

resume_text = input("Paste your resume text:\n")

skills = extract_skills(resume_text)
suggestions = suggest_improvements(skills)

print("\nDetected Skills:", skills)

print("\nSuggestions:")
for s in suggestions:
    print("-", s)
