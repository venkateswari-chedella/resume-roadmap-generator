def generate_resume(data):

    resume = f"""
{data["name"].upper()}

Email: {data["email"]}
Phone: {data["phone"]}

PROFESSIONAL SUMMARY
Motivated and hardworking candidate seeking opportunities to
build professional experience and contribute technical skills
to a growth-oriented organization.

EDUCATION
{data["education"]}

TECHNICAL SKILLS
{data["skills"]}

PROJECTS
{data["projects"]}

EXPERIENCE
{data["experience"]}

CAREER OBJECTIVE
{data["career_goal"]}

DECLARATION
I hereby declare that the information provided above is true
and correct to the best of my knowledge.
"""

    return resume.strip()
