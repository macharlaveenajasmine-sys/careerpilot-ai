from agents.career_mentor import generate_career_guidance
from agents.resume_agent import analyze_resume
from agents.skill_gap_agent import analyze_skill_gap
from agents.roadmap_agent import generate_roadmap
from agents.interview_agent import interview_preparation


def process_request(career_goal, question="", resume_text=None):
    """
    CareerPilot AI Orchestrator

    Runs every AI agent and returns one complete report.
    """

    report = {}

    if resume_text:

        report["resume"] = analyze_resume(resume_text)

        report["skill_gap"] = analyze_skill_gap(
            resume_text,
            career_goal
        )

        report["roadmap"] = generate_roadmap(
            resume_text,
            career_goal
        )

        report["interview"] = interview_preparation(
            resume_text,
            career_goal
        )

    report["guidance"] = generate_career_guidance(
        career_goal,
        question
    )

    return report