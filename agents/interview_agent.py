from utils.gemini_client import client


def interview_preparation(resume_text, career_goal):

    prompt = f"""
You are an expert technical interviewer.

Career Goal:
{career_goal}

Resume:

{resume_text}

Generate:

## 🎤 HR Interview Questions

## 💻 Technical Interview Questions

## 🧠 Coding Preparation Tips

## ⚠️ Common Mistakes

## 🚀 Final Interview Advice
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text