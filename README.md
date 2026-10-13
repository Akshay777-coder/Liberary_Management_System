 <h1>📚 Library Management System</h1>

<p>A simple Library Management System built using Python and SQLite. This project allows users to add, display, update, and delete books and library members through a menu-driven command-line interface.</p>

<h2>📌 Project Overview</h2>

<p>The project has two main modules:</p>

<ul>
  <li>Books Management: Manage book records.</li>
  <li>Members Management: Manage library member records.</li>
</ul>

<p>All records are stored in an SQLite database.</p>

<h2>🛠️ Technologies Used</h2>

<ul>
  <li>Python</li>
  <li>SQLite3</li>
  <li>OS Module</li>
  <li>Sys Module</li>
</ul>

<h2>📂 Project Structure</h2>

<pre>
Library_Management_System/
│
├── main.py
├── liberary.py
├── database/
│   └── liberary.db
│
└── README.md
</pre>

<p>Note: Replace <code>main.py</code> with the actual filename of your main Python program if it is different.</p>

<h2>⚙️ How to Run the Project</h2>

<h3>1. Install Python</h3>

<p>Download and install Python from the official website:</p>

<p><a href="https://www.python.org/downloads/">Download Python</a></p>

<h3>2. Clone the Repository</h3>

<pre>
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
</pre>

<p>Replace the repository URL with your actual GitHub repository URL.</p>

<h3>3. Open the Project Directory</h3>

<pre>
cd YOUR_REPOSITORY
</pre>

<h3>4. Run the Program</h3>

<pre>
python main.py
</pre>

<p>No additional Python packages are required because all modules used in this project are included in Python's standard library.</p>

<h2>📖 Code Modules</h2>

<h3>1. liberary.py — Database Module</h3>

<p>This module manages the SQLite database, creates tables, and performs database operations.</p>

<table>
  <thead>
    <tr>
      <th>Function</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>create_db()</code></td>
      <td>Connects to the SQLite database.</td>
    </tr>
    <tr>
      <td><code>create_table_books()</code></td>
      <td>Creates the books table.</td>
    </tr>
    <tr>
      <td><code>create_table_members()</code></td>
      <td>Creates the members table.</td>
    </tr>
    <tr>
      <td><code>insert_into_books()</code></td>
      <td>Adds a new book.</td>
    </tr>
    <tr>
      <td><code>display_books()</code></td>
      <td>Displays all books.</td>
    </tr>
    <tr>
      <td><code>update_books()</code></td>
      <td>Updates an existing book.</td>
    </tr>
    <tr>
      <td><code>delete_book()</code></td>
      <td>Deletes a book by its ID.</td>
    </tr>
    <tr>
      <td><code>insert_into_members()</code></td>
      <td>Adds a new library member.</td>
    </tr>
    <tr>
      <td><code>display_members()</code></td>
      <td>Displays all members.</td>
    </tr>
    <tr>
      <td><code>update_members()</code></td>
      <td>Updates an existing member.</td>
    </tr>
    <tr>
      <td><code>delete_members()</code></td>
      <td>Deletes a member by their ID.</td>
    </tr>
  </tbody>
</table>

<h3>2. Main Python File — Application Module</h3>

<p>This module provides the menus and accepts user input.</p>

<ul>
  <li><code>books()</code> — Opens the book management menu.</li>
  <li><code>members()</code> — Opens the member management menu.</li>
  <li><code>main()</code> — Displays the main menu and directs the user to the selected section.</li>
</ul>

<p>The program uses <code>while</code> loops to keep menus running and <code>match-case</code> statements to process user choices.</p>

<h2>🗄️ Database Structure</h2>

<h3>Books Table</h3>

<table>
  <thead>
    <tr>
      <th>Column</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>book_id</code></td>
      <td>Unique ID for each book, generated automatically.</td>
    </tr>
    <tr>
      <td><code>title</code></td>
      <td>Title of the book.</td>
    </tr>
    <tr>
      <td><code>author</code></td>
      <td>Name of the author.</td>
    </tr>
    <tr>
      <td><code>is_issued</code></td>
      <td>0 means available; 1 means issued.</td>
    </tr>
    <tr>
      <td><code>price</code></td>
      <td>Price of the book.</td>
    </tr>
  </tbody>
</table>

<h3>Members Table</h3>

<table>
  <thead>
    <tr>
      <th>Column</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>member_id</code></td>
      <td>Unique ID for each member, generated automatically.</td>
    </tr>
    <tr>
      <td><code>name</code></td>
      <td>Name of the member.</td>
    </tr>
    <tr>
      <td><code>email</code></td>
      <td>Email address of the member.</td>
    </tr>
    <tr>
      <td><code>number</code></td>
      <td>Contact number of the member.</td>
    </tr>
  </tbody>
</table>

<h2>🔄 CRUD Operations</h2>

<p>CRUD stands for Create, Read, Update, and Delete.</p>

<h3>➕ Add (Create)</h3>

<p>Adds a new book or member to the database. The program accepts the required details and inserts the record into the appropriate table.</p>

<h3>📋 Display (Read)</h3>

<p>Retrieves and displays all records from the selected table using SQL SELECT queries.</p>

<h3>✏️ Update</h3>

<p>Updates an existing book or member using its unique ID. The user enters the new details, which are saved in the database.</p>

<h3>🗑️ Delete</h3>

<p>Deletes a book or member using its unique ID. The program requests confirmation before deleting the selected record.</p>

<h2>🖥️ Main Menu</h2>

<pre>
*** Welcome to the Library Management System ***

1. Books
2. Members
3. Exit
</pre>

<p>Select Books to manage book records, Members to manage member records, or Exit to close the program.</p>

<h2>🚀 Future Improvements</h2>

<ul>
  <li>Add a search feature for books and members.</li>
  <li>Validate email addresses and contact numbers.</li>
  <li>Implement book issuing and returning functionality.</li>
  <li>Display database records in a formatted table.</li>
  <li>Add administrator login functionality.</li>
</ul>

<h2>👨‍💻 Author</h2>

<p>Akshay Kumar</p>
<p>BCA Student | Python | SQL | Database Management</p>

<h2>📄 License</h2>

<p>This project is intended for educational and learning purposes.</p>
