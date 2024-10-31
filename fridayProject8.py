import tkinter as tk
from tkinter import ttk
import sqlite3
from tkinter import messagebox

connection = sqlite3.connect('feedback.db')
cursor = connection.cursor()
root = tk.Tk()
databaseLocked = True

style = ttk.Style(root)
style.theme_use("clam")

cursor.execute('''
CREATE TABLE IF NOT EXISTS feedbackTable (
    name BLOB NOT NULL,
    email BLOB NOT NULL,
    feedback BLOB
)
''')
connection.commit()

class FeedbackApp:
    def __init__(self, root):
        self.root = root

        self.root.title("Customer Feedback")
        self.root.geometry("400x450")
        
        # Label and entry for Name
        tk.Label(root, text="Name:", font=("Arial", 10)).pack(pady=5)
        self.name_entry = ttk.Entry(root, width=40)
        self.name_entry.pack(pady=5)
        
        # Label and entry for Email
        tk.Label(root, text="Email:", font=("Arial", 10)).pack(pady=5)
        self.email_entry = ttk.Entry(root, width=40)
        self.email_entry.pack(pady=5)
        
        # Label and Text box for Feedback
        tk.Label(root, text="Your Feedback:", font=("Arial", 10)).pack(pady=5)
        self.feedback_text = tk.Text(root, height=10, width=40)
        self.feedback_text.pack(pady=5)
        
        # Submit Button
        self.submit_button = ttk.Button(root, text="Submit", command=self.submit_feedback)
        self.submit_button.pack(pady=10)

        self.database_button = ttk.Button(root, text="View Database", command=self.view_database)
        self.database_button.pack(pady=0)
    def submit_feedback(self):
        # Get user inputs
        name = self.name_entry.get()
        email = self.email_entry.get()
        feedback = self.feedback_text.get("1.0", tk.END).strip()
        fullFeedback = [name, email, feedback]
        try:
            cursor.execute('''
            INSERT INTO feedbackTable (name, email, feedback) VALUES (?, ?, ?)
            ''', fullFeedback)
            connection.commit()
            print("Feedback added successfully!")

        except sqlite3.IntegrityError as e:
            print(f"IntegrityError: {e}. This feedback has already given.")
        
        print("Customer Feedback:")
        print(f"Name: {name}")
        print(f"Email: {email}")
        print("Feedback:", feedback)
        print("-" * 40)  # Separator for readability in console
        
        # Clear the input fields
        self.name_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.feedback_text.delete("1.0", tk.END)
        
        # Show confirmation message
        messagebox.showinfo("Feedback Submitted", "Thank you for your feedback!")
    def view_database(self):
        try:
            cursor.execute('SELECT * FROM feedbackTable')

            data = cursor.fetchall()

            print(data)
        except sqlite3.Error as e:
            print(f"Database error: {e}")
      
if __name__ == "__main__":
    app = FeedbackApp(root)
    root.mainloop()
