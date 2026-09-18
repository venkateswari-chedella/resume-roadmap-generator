import os
import tkinter as tk

from tkinter import messagebox

from database import create_database, save_user
from resume_generator import generate_resume
from roadmap_generator import generate_roadmap
from pdf_generator import create_pdf


# -----------------------------
# Database initialization
# -----------------------------

create_database()


# -----------------------------
# Main window
# -----------------------------

root = tk.Tk()

root.title("Resume & Career Roadmap Generator")

root.geometry("700x750")

root.configure(bg="#f1f5f9")


# -----------------------------
# Title
# -----------------------------

title = tk.Label(
    root,
    text="Resume & Career Roadmap Generator",
    font=("Arial", 22, "bold"),
    bg="#f1f5f9",
    fg="#1e3a8a"
)

title.pack(pady=20)


subtitle = tk.Label(
    root,
    text="Create your professional resume and career roadmap",
    font=("Arial", 11),
    bg="#f1f5f9",
    fg="#475569"
)

subtitle.pack(pady=(0, 15))


# -----------------------------
# Form frame
# -----------------------------

form_frame = tk.Frame(
    root,
    bg="white",
    padx=25,
    pady=20
)

form_frame.pack(
    padx=30,
    pady=10,
    fill="both"
)


entries = {}


fields = [
    ("Name", "name"),
    ("Email", "email"),
    ("Phone", "phone"),
    ("Education", "education"),
    ("Skills", "skills"),
    ("Projects", "projects"),
    ("Experience", "experience"),
    ("Career Goal", "career_goal")
]


# -----------------------------
# Create input fields
# -----------------------------

for row, (label_text, key) in enumerate(fields):

    label = tk.Label(
        form_frame,
        text=label_text,
        font=("Arial", 11, "bold"),
        bg="white",
        fg="#334155"
    )

    label.grid(
        row=row,
        column=0,
        sticky="w",
        padx=10,
        pady=7
    )

    entry = tk.Entry(
        form_frame,
        width=50,
        font=("Arial", 10),
        relief="solid",
        bd=1
    )

    entry.grid(
        row=row,
        column=1,
        padx=10,
        pady=7
    )

    entries[key] = entry


# -----------------------------
# Generate function
# -----------------------------

def generate_documents():

    data = {
        "name": entries["name"].get().strip(),
        "email": entries["email"].get().strip(),
        "phone": entries["phone"].get().strip(),
        "education": entries["education"].get().strip(),
        "skills": entries["skills"].get().strip(),
        "projects": entries["projects"].get().strip(),
        "experience": entries["experience"].get().strip(),
        "career_goal": entries["career_goal"].get().strip()
    }


    # Validation

    if not data["name"]:
        messagebox.showerror(
            "Error",
            "Please enter your name."
        )
        return


    if not data["email"]:
        messagebox.showerror(
            "Error",
            "Please enter your email."
        )
        return


    if not data["career_goal"]:
        messagebox.showerror(
            "Error",
            "Please enter your career goal."
        )
        return


    try:

        # Save user

        save_user(data)


        # Generate resume

        resume = generate_resume(data)


        safe_name = (
            data["name"]
            .replace(" ", "_")
            .replace("/", "_")
            .replace("\\", "_")
        )


        resume_path = os.path.join(
            "output",
            "resumes",
            f"{safe_name}_Resume.pdf"
        )


        create_pdf(
            resume_path,
            "PROFESSIONAL RESUME",
            resume
        )


        # Generate roadmap

        roadmap = generate_roadmap(
            data["career_goal"]
        )


        roadmap_path = os.path.join(
            "output",
            "roadmaps",
            f"{safe_name}_Career_Roadmap.pdf"
        )


        create_pdf(
            roadmap_path,
            "CAREER ROADMAP",
            roadmap
        )


        # Success message

        messagebox.showinfo(
            "Success",
            "Documents generated successfully!\n\n"
            f"Resume:\n{resume_path}\n\n"
            f"Career Roadmap:\n{roadmap_path}"
        )


    except Exception as error:

        messagebox.showerror(
            "Error",
            f"Something went wrong:\n\n{error}"
        )


# -----------------------------
# Generate button
# -----------------------------

generate_button = tk.Button(
    root,
    text="GENERATE RESUME & ROADMAP",
    command=generate_documents,
    font=("Arial", 12, "bold"),
    bg="#2563eb",
    fg="white",
    activebackground="#1d4ed8",
    activeforeground="white",
    padx=25,
    pady=12,
    relief="flat",
    cursor="hand2"
)

generate_button.pack(pady=25)


# -----------------------------
# Footer
# -----------------------------

footer = tk.Label(
    root,
    text="Python • Tkinter • SQLite • ReportLab",
    font=("Arial", 9),
    bg="#f1f5f9",
    fg="#64748b"
)

footer.pack(pady=5)


# -----------------------------
# Start application
# -----------------------------

root.mainloop()
