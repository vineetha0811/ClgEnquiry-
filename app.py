"""
app.py
======
Main Flask application for the College Enquiry Chatbot.

Routes:
    /                    -> shows the enquiry page
    /category/<name>     -> shows one topic (from SQLite)
    /ask                 -> answers a typed question (keyword matching)

How to run:
    python app.py
    Then open http://127.0.0.1:5000 in your browser.
"""

from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


def get_db_connection():
    """Open a connection to the SQLite database."""
    conn = sqlite3.connect("college.db")
    conn.row_factory = sqlite3.Row   # lets us read columns by name
    return conn


def get_enquiry_by_category(category):
    """Fetch the enquiry record that matches a category (case-insensitive)."""
    conn = get_db_connection()
    row = conn.execute(
        "SELECT * FROM enquiries WHERE LOWER(category) = LOWER(?) LIMIT 1",
        (category,)
    ).fetchone()
    conn.close()
    return row


def get_enquiry_by_question(question):
    """Find the best matching enquiry using simple keyword matching."""
    q = question.lower()

    # Each group of keywords maps to a category in the database.
    keyword_rules = [
        (("admission", "apply", "application", "counselling"), "Admissions"),
        (("course", "courses", "program", "programs", "degree"), "Courses"),
        (("fee", "fees", "tuition", "pay", "cost"), "Fees"),
        (("scholarship", "scholarships"), "Scholarships"),
        (("hostel", "accommodation"), "Hostel"),
        (("placement", "placements", "job", "jobs", "recruitment", "career"), "Placements"),
        (("contact", "phone", "email", "help desk", "call"), "Contact"),
    ]

    # If any keyword appears in the question, return that category's info.
    for keywords, category in keyword_rules:
        for keyword in keywords:
            if keyword in q:
                return get_enquiry_by_category(category)

    return None  # no keyword matched


@app.route("/")
def index():
    """Show the main page (no answer yet)."""
    return render_template(
        "index.html",
        answer_title=None,
        answer_content=None,
        user_question=None,
    )


@app.route("/category/<category>")
def category_page(category):
    """Show information for a clicked navigation topic."""
    row = get_enquiry_by_category(category)

    if row:
        title = row["title"]
        content = row["content"]
    else:
        title = category
        content = "Sorry, that topic is not available."

    return render_template(
        "index.html",
        answer_title=title,
        answer_content=content,
        user_question=None,
    )


@app.route("/ask", methods=["POST"])
def ask():
    """Handle a question typed by the user."""
    question = request.form.get("question", "").strip()

    # Do not allow empty questions.
    if not question:
        return render_template(
            "index.html",
            answer_title="No Answer",
            answer_content="Please type a question first.",
            user_question=None,
        )

    # Try to find a matching answer in the database.
    row = get_enquiry_by_question(question)

    if row:
        answer_title = row["title"]
        answer_content = row["content"]
    else:
        # No keyword matched -> show a friendly fallback message.
        answer_title = "No Answer"
        answer_content = ("Sorry, I could not understand your question. "
                          "Please choose one of the available topics.")

    return render_template(
        "index.html",
        answer_title=answer_title,
        answer_content=answer_content,
        user_question=question,
    )


if __name__ == "__main__":
    # debug=True shows errors in the browser while developing.
    app.run(debug=True)