def critique_prompt(text):
    return f"""
You are a resume reviewer. Analyze the following resume content and provide feedback on:
1. Tone and clarity
2. Formatting or structure issues
3. Missing elements (skills, metrics, action verbs)
Also, highlight weak areas and suggest improvements.

Resume Text:
{text}
"""

def rewrite_prompt(section):
    return f"""
Improve the following section of a resume for clarity and impact. Use strong action verbs, quantify results, and make it ATS-friendly.

Section:
{section}
"""
