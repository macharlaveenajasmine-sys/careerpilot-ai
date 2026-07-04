from agents.career_mentor import generate_career_guidance


def process_request(career_goal, question):
    """
    Career Manager Agent

    This agent acts as the central controller.
    """

    return generate_career_guidance(career_goal, question)