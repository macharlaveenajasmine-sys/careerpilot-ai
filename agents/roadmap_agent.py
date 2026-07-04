from utils.gemini_client import client


def generate_roadmap(resume_text, career_goal):

    prompt = f"""
You are an expert career roadmap planner.

Career Goal:
{career_goal}

Resume:

{resume_text}

Create a personalized roadmap.

Include:

## 🎯 Current Level

## 📚 Skills to Learn

## 🏆 Certifications

## 💻 Projects

## 📅 30-Day Plan

## 📅 90-Day Plan

## 🚀 6-Month Goal
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text