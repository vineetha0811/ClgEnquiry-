"""
init_db.py
==========
Run this file ONCE to create the SQLite database (college.db)
and insert all the college enquiry information.

How to run:
    python init_db.py
"""

import sqlite3

# 1) Connect to the database.
#    If college.db does not exist, SQLite creates it automatically.
conn = sqlite3.connect("college.db")
cursor = conn.cursor()

# 2) Create the enquiries table (if it does not already exist).
cursor.execute("""
    CREATE TABLE IF NOT EXISTS enquiries (
        id       INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT    NOT NULL,   -- e.g. Admissions, Courses, Fees ...
        title    TEXT    NOT NULL,   -- e.g. Admission Process
        content  TEXT    NOT NULL    -- the actual answer text
    )
""")

# 3) Remove any old rows so the table is re-seeded fresh each time.
cursor.execute("DELETE FROM enquiries")

# 4) Insert the college information for all 7 categories.
enquiries = [
    (
        "Admissions",
        "Admission Process",
        "Admissions are open for UG and PG programs. "
        "Students can apply online, upload required documents, "
        "pay the application fee, and attend counselling if shortlisted."
    ),
    (
        "Courses",
        "Courses Offered",
        "Available programs include B.Tech, B.Sc, B.Com, B.E., "
        "M.Tech, MBA, M.Sc, and MCA."
    ),
    (
        "Fees",
        "Fee Structure",
        "B.Tech - Rs 80,000 per year\n"
        "B.Sc - Rs 40,000 per year\n"
        "B.Com - Rs 35,000 per year\n"
        "MBA - Rs 70,000 per year\n"
        "MCA - Rs 60,000 per year"
    ),
    (
        "Scholarships",
        "Scholarships",
        "Merit Scholarship\n"
        "Government Scholarship\n"
        "Sports Scholarship\n"
        "Need-Based Scholarship"
    ),
    (
        "Hostel",
        "Hostel Facilities",
        "Separate hostel facilities for boys and girls\n"
        "Mess facility\n"
        "Wi-Fi facility\n"
        "Security\n"
        "Study rooms"
    ),
    (
        "Placements",
        "Placements",
        "Placement assistance\n"
        "Campus recruitment\n"
        "Training and placement cell\n"
        "Aptitude training\n"
        "Technical training\n"
        "Interview preparation"
    ),
    (
        "Contact",
        "Contact Us",
        "College Enquiry Help Desk\n"
        "Phone: +91 98765 43210\n"
        "Email: admissions@college.edu\n"
        "Office Hours: 9:00 AM to 5:00 PM"
    ),
]

# 5) Insert all rows in one go using a parameterized query.
cursor.executemany(
    "INSERT INTO enquiries (category, title, content) VALUES (?, ?, ?)",
    enquiries
)

# 6) Save the changes and close the connection.
conn.commit()
conn.close()

print("college.db created and seeded with", len(enquiries), "enquiries.")