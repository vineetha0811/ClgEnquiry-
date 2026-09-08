# College Enquiry Chatbot

A simple college admissions enquiry assistant built with **Python Flask** and **SQLite**.
Students can click a topic (Admissions, Courses, Fees, Scholarships, Hostel, Placements, Contact)
or type a question, and the site shows the matching information from the database.

## Project Structure

```
college_enquiry_chatbot/
│
├── app.py            # Main Flask application
├── init_db.py        # Creates college.db and inserts the sample data
├── requirements.txt  # List of Python packages needed
├── college.db        # SQLite database (created by init_db.py)
│
├── templates/        # HTML files (Jinja2 templates)
│   ├── index.html    # Main page
│   └── result.html   # Answer block (shown after a question)
│
└── static/
    └── style.css     # Stylesheet
```

## How the Data Flows

```
User
  ↓  (clicks a topic or types a question)
HTML form / link
  ↓
Flask (app.py)
  ↓  (SQL query / keyword matching)
SQLite database (college.db)
  ↓
Flask response (rendered HTML)
  ↓
Browser
```

---

## How to Run on Windows

### Step 1 - Install Python
- Download Python from https://www.python.org/downloads/
- During installation, tick **"Add Python to PATH"**.
- Open **Command Prompt** and check with:  `python --version`

### Step 2 - Create the project folder
Put the files in a folder named `college_enquiry_chatbot`
(or extract the zip there).

### Step 3 - Install Flask
Open Command Prompt inside the project folder and run:
```
pip install flask
```
(or `pip install -r requirements.txt`)

### Step 4 - Initialize the database
This creates `college.db` and adds all the college information:
```
python init_db.py
```

### Step 5 - Start the server
```
python app.py
```
You should see output like `Running on http://127.0.0.1:5000`.

### Step 6 - Open the website
Open your browser and go to:
```
http://127.0.0.1:5000
```

Now you can:
- Click any topic in the navigation bar, OR
- Click a quick option (`admission process`, `courses offered`, `fee structure`), OR
- Type a question like *"What is the admission process?"* and press Send.

### Step 7 - Stop the server
Go back to the Command Prompt window and press **Ctrl + C**.

---

## Example Questions

| You type | You get |
|----------|---------|
| What is the admission process? | Admission Process |
| What courses are available? | Courses Offered |
| What are the fees? | Fee Structure |
| Tell me about scholarships | Scholarships |
| Is hostel available? | Hostel Facilities |
| How are the placements? | Placements |
| How can I contact the college? | Contact Us |