from utils.gemini_client import client


def analyze_skill_gap(resume_text, career_goal):

    prompt = f"""
You are an expert career advisor.

Career Goal:
{career_goal}

Resume:

{resume_text}

Compare the user's current skills with the skills needed.

Provide:

## ✅ Current Skills

## ❌ Missing Skills

## 📚 Recommended Certifications

## 💻 Recommended Projects
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text