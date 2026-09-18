import pandas as pd
# Load student data
students = pd.read_csv("../data/students.csv")
# Required skills for Data Analyst
required_skills = ["SQL", "Python", "Excel", "Power_BI"]
# Calculate Skill Match %
students["Skill_Match_%"] = (
    students[required_skills].sum(axis=1) / len(required_skills) * 100
)
# Find missing skills
def find_missing_skills(row):
    missing = []
    for skill in required_skills:
        if row[skill] == 0:
            missing.append(skill)

    return ", ".join(missing) if missing else "None"
students["Missing_Skills"] = students.apply(find_missing_skills, axis=1)
# Readiness status
def readiness(match):
    if match >= 75:
        return "Ready"
    elif match >= 50:
        return "Almost Ready"
    else:
        return "Needs Improvement"

students["Readiness_Status"] = students["Skill_Match_%"].apply(readiness)
# Display result
print("\n===== INTERNSHIP SKILL GAP ANALYSIS =====\n")
print(
    students[
        [
            "Student_ID",
            "Student_Name",
            "CGPA",
            "Skill_Match_%",
            "Missing_Skills",
            "Readiness_Status",
        ]
    ].to_string(index=False)
)
# Save output
students.to_csv("../data/skill_gap_result.csv", index=False)
print("\nAnalysis completed successfully!")
print("Result saved in data/skill_gap_result.csv")