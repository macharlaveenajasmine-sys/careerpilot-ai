from utils.gemini_client import client


def generate_career_guidance(career_goal, question):

    prompt = f"""
You are CareerPilot AI, an expert career mentor.

Career Goal:
{career_goal}

User Question:
{question}

Provide:

## 🎯 Career Advice

## 📚 Skills to Learn

## 🚀 Recommended Certifications

## 💼 Career Opportunities

## 📅 Next Steps
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text