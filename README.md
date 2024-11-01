# fridayProject8 
passowrd = password

Overview:
The FeedbackApp is a graphical user interface (GUI) application built with Python's tkinter library, which allows users to submit customer feedback including their name, email, and feedback text. The application stores this information in an SQLite database (feedback.db) for easy retrieval and review.

Prerequisites
Ensure that you have Python installed, along with the tkinter and sqlite3 libraries (both are included with Python by default).

Application Structure and Key Features
The application has two main functions:

Collecting Feedback: Users can enter their name, email, and feedback in designated fields and submit it to be stored in the database.
Viewing Database Content: A protected feature that requires a password allows access to view all feedback entries directly from the database.
Code Structure
The application code is organized as follows:

Database Setup

Connects to an SQLite database (feedback.db).
Creates a table called feedbackTable if it doesn’t exist, with columns for name, email, and feedback.
FeedbackApp Class

Initializes the FeedbackApp class which handles the GUI layout and interaction.
Sets up the window title, dimensions, and styles.
Contains methods for user interactions:
submit_feedback(): Handles submission of feedback to the database.
view_database(): Allows an authorized user to view all feedback entries in the database.
Detailed Code Walkthrough
1. GUI Initialization
The app window is created and styled.
Fields for Name, Email, and Feedback are added, each with a label.
A Submit button saves the feedback to the database, and a View Database button allows viewing all entries (password-protected).
2. Submitting Feedback
submit_feedback() method:
Retrieves the user’s inputs from the entry fields.
Inserts the feedback into feedbackTable in the database.
Clears the entry fields after submission and shows a confirmation message.
Prints the feedback details in the console for immediate feedback during development.
3. Viewing the Database
view_database() method:
Prompts for a password ("password") to access the database entries.
If correct, retrieves and prints all entries in the feedbackTable.
If an error occurs (e.g., database connection issues), an error message is printed.
How to Run the Application
Run the Application:
Execute the script in your Python environment. A window titled "Customer Feedback" will appear.
Enter Feedback:
In the app window, enter your name, email, and feedback text, then press the Submit button to save.
View Database Entries (Optional):
Click on the View Database button.
Enter the password (password) when prompted in the console.
If the password is correct, all database entries will be displayed in the console.
