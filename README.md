📚 Book Management System

A simple Python-based Book Management System that allows users to manage book records using a SQLite database.
This project demonstrates database operations such as insertion, retrieval, updating, and searching using Python.

📌 Project Description

The Book Management System is a console-based application developed in Python.
It allows users to:

Add new books

View all books

Search books by title or author

Update book details

Store data persistently using SQLite

This project is ideal for learning:

Python programming

Database integration

CRUD operations

File handling

🚀 Features

✔ Add new book records
✔ View all available books
✔ Search books by title
✔ Search books by author
✔ Update book information
✔ Persistent storage using SQLite database

🛠️ Technologies Used

Programming Language: Python 3.x

Database: SQLite3

Libraries Used:

sqlite3 (built-in)

csv (for dataset handling)

📂 Project Structure
BookManagementSystem/
│
├── BK_System.py        # Main application file
├── db_setup.py         # Database initialization script
├── model.py            # Database functions (CRUD operations)
├── book_data.csv       # Sample dataset
├── books.db            # SQLite database
├── requirements.txt    # Project dependencies
└── README.md
⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/Selvaragavanvsbec/BookManagementSystem.git
cd BookManagementSystem
2️⃣ Create Virtual Environment (Optional but Recommended)
python -m venv venv

Activate environment:

Windows

venv\Scripts\activate

Mac/Linux

source venv/bin/activate
3️⃣ Install Requirements
pip install -r requirements.txt
4️⃣ Initialize Database
python db_setup.py

This will create the books.db file.

5️⃣ Run the Application
python BK_System.py
🖥️ How It Works

The system connects to a SQLite database.

Tables are created if not already present.

Users interact through a menu-driven console interface.

All book records are stored in books.db.

📊 Example Menu
1. Add Book
2. View All Books
3. Search Book
4. Update Book
5. Exit
🔮 Future Improvements

Add delete book feature

Implement user authentication

Add graphical user interface (GUI)

Convert to web-based application using Flask/Django

Integrate book recommendation feature

👨‍💻 Author

Selvaragavan
GitHub: https://github.com/Selvaragavanvsbec

📜 License

This project is open-source. You may add an MIT License file if required.

