from utils.gemini_client import client


def analyze_resume(resume_text):

    prompt = f"""
You are an expert Resume Reviewer and ATS Expert.

Analyze the resume below.

Resume:

{resume_text}

Return:

## 📌 Resume Strengths

## ⚠️ Weaknesses

## 📚 Missing Skills

## 🚀 Suggestions

## 🎯 Resume Score (out of 10)
"""

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:

        return f"""
### ⚠️ Error

{str(e)}
"""