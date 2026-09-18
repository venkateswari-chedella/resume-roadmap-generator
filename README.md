Resume & Roadmap Generator

A Python-based desktop application for generating professional resumes and personalized career roadmaps.

Features

Professional resume generation

Career-specific roadmap generation

Resume PDF export

Career roadmap PDF export

SQLite database for storing user information

Simple Tkinter graphical interface

Multiple career paths

JSON-based roadmap templates

Technologies

Python

Tkinter

SQLite

ReportLab

JSON

Project Structure
Resume_Roadmap_Generator/
│
├── main.py
├── resume_generator.py
├── roadmap_generator.py
├── pdf_generator.py
├── database.py
│
├── templates/
│   ├── resume_template.json
│   └── roadmap_data.json
│
├── output/
│   ├── resumes/
│   └── roadmaps/
│
└── database/

How to Run

Install the required package:

python -m pip install reportlab


Run the application:

python main.py

Output

The application generates:

Professional resume PDF files in output/resumes/

Career roadmap PDF files in output/roadmaps/

User information is stored locally using SQLite.

Author

Venkateswari Chedella
