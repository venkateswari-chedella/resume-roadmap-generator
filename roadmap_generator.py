import json
import os


ROADMAP_FILE = "templates/roadmap_data.json"


def load_roadmaps():

    if not os.path.exists(ROADMAP_FILE):
        return {}

    with open(ROADMAP_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def generate_roadmap(career_goal):

    roadmaps = load_roadmaps()

    key = career_goal.lower().strip()

    if key in roadmaps:
        steps = roadmaps[key]
    else:
        steps = [
            "Learn the fundamentals of your chosen field",
            "Learn intermediate concepts",
            "Practice with small projects",
            "Build real-world projects",
            "Create a GitHub portfolio",
            "Improve your communication skills",
            "Prepare your resume",
            "Practice technical interviews",
            "Apply for internships and jobs",
            "Continue learning advanced concepts"
        ]

    roadmap = f"""
CAREER ROADMAP
===============

TARGET ROLE
{career_goal.upper()}

LEARNING ROADMAP
"""

    for number, step in enumerate(steps, start=1):
        roadmap += f"\n{number}. {step}"

    roadmap += """

PROJECT PHASE
=============

After learning the required concepts:

1. Build a beginner project.
2. Build an intermediate project.
3. Build a real-world project.
4. Upload projects to GitHub.
5. Add the best projects to your resume.

JOB PREPARATION
===============

1. Prepare your resume.
2. Create a professional GitHub profile.
3. Practice interview questions.
4. Practice coding problems.
5. Apply for internships and jobs.
"""

    return roadmap.strip()
