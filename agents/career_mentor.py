import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


def generate_career_guidance(career_goal, question):
    prompt = f"""
    The user's career goal is {career_goal}.

    User Question:
    {question}

    Give:
    1. Career Advice
    2. Skills Required
    3. Learning Resources
    4. Suggested Projects
    5. Interview Preparation Tips
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text