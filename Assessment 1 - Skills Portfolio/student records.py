import tkinter as tk
from tkinter import ttk, messagebox
import csv
import os

# --- CONFIGURATION ---
CSV_FILE = "student_data.csv"

# This is the data provided in your request
INITIAL_DATA = """StudentID,FirstName,LastName,Age,Gender,Grade,Email
1001,Liam,Smith,16,Male,10,liam.smith@example.com
1002,Emma,Johnson,17,Female,11,emma.johnson@example.com
1003,Noah,Williams,15,Male,9,noah.williams@example.com
1004,Olivia,Jones,16,Female,10,olivia.jones@example.com
1005,William,Brown,17,Male,11,william.brown@example.com
1006,Ava,Davis,15,Female,9,ava.davis@example.com
1007,James,Miller,16,Male,10,james.miller@example.com
1008,Sophia,Wilson,17,Female,11,sophia.wilson@example.com
1009,Benjamin,Moore,15,Male,9,benjamin.moore@example.com
1010,Isabella,Taylor,16,Female,10,isabella.taylor@example.com
1011,Elijah,Anderson,17,Male,11,elijah.anderson@example.com
1012,Mia,Thomas,15,Female,9,mia.thomas@example.com
1013,Lucas,Jackson,16,Male,10,lucas.jackson@example.com
1014,Charlotte,White,17,Female,11,charlotte.white@example.com
1015,Mason,Harris,15,Male,9,mason.harris@example.com
1016,Amelia,Martin,16,Female,10,amelia.martin@example.com
1017,Logan,Thompson,17,Male,11,logan.thompson@example.com
1018,Evelyn,Garcia,15,Female,9,evelyn.garcia@example.com
1019,Alexander,Martinez,16,Male,10,alexander.martinez@example.com
1020,Harper,Robinson,17,Female,11,harper.robinson@example.com
1021,Ethan,Clark,15,Male,9,ethan.clark@example.com
1022,Abigail,Rodriguez,16,Female,10,abigail.rodriguez@example.com
1023,Jacob,Lewis,17,Male,11,jacob.lewis@example.com
1024,Emily,Lee,15,Female,9,emily.lee@example.com
1025,Michael,Walker,16,Male,10,michael.walker@example.com
1026,Elizabeth,Hall,17,Female,11,elizabeth.hall@example.com
1027,Daniel,Allen,15,Male,9,daniel.allen@example.com
1028,Sofia,Young,16,Female,10,sofia.young@example.com
1029,Matthew,Hernandez,17,Male,11,matthew.hernandez@example.com
1030,Avery,King,15,Female,9,avery.king@example.com
1031,David,Wright,16,Male,10,david.wright@example.com
1032,Scarlett,Lopez,17,Female,11,scarlett.lopez@example.com
1033,Joseph,Hill,15,Male,9,joseph.hill@example.com
1034,Victoria,Scott,16,Female,10,victoria.scott@example.com
1035,Samuel,Green,17,Male,11,samuel.green@example.com
1036,Lillian,Adams,15,Female,9,lillian.adams@example.com
1037,Henry,Baker,16,Male,10,henry.baker@example.com
1038,Aria,Gonzalez,17,Female,11,aria.gonzalez@example.com
1039,Owen,Nelson,15,Male,9,owen.nelson@example.com
1040,Chloe,Carter,16,Female,10,chloe.carter@example.com
1041,Gabriel,Mitchell,17,Male,11,gabriel.mitchell@example.com
1042,Ella,Perez,15,Female,9,ella.perez@example.com
1043,Carter,Roberts,16,Male,10,carter.roberts@example.com
1044,Madison,Turner,17,Female,11,madison.turner@example.com
1045,Wyatt,Phillips,15,Male,9,wyatt.phillips@example.com
1046,Emily,Campbell,16,Female,10,emily.campbell@example.com
1047,Caleb,Parker,17,Male,11,caleb.parker@example.com
1048,Grace,Evans,15,Female,9,grace.evans@example.com
1049,Jayden,Edwards,16,Male,10,jayden.edwards@example.com
1050,Hannah,Collins,17,Female,11,hannah.collins@example.com"""

# Initialize CSV file if it doesn't exist
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, "w", newline="", encoding="utf-8") as file:
        file.write(INITIAL_DATA)

class StudentRecordsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1000x600")
        
        # Variables
        self.id_var = tk.StringVar()
        self.fname_var = tk.StringVar()
        self.lname_var = tk.StringVar()
        self.age_var = tk.StringVar()
        self.gender_var = tk.StringVar()
        self.grade_var = tk.StringVar()
        self.email_var = tk.StringVar()

        # Form Frame
        form_frame = tk.LabelFrame(root, text="Student Details", padx=10, pady=10)
        form_frame.pack(fill="x", padx=10, pady=5)

        # Row 0
        tk.Label(form_frame, text="Student ID").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        tk.Entry(form_frame, textvariable=self.id_var).grid(row=0, column=1, padx=5, pady=5, sticky="w")

        tk.Label(form_frame, text="Age").grid(row=0, column=2, padx=5, pady=5, sticky="e")
        tk.Entry(form_frame, textvariable=self.age_var).grid(row=0, column=3, padx=5, pady=5, sticky="w")
        
        tk.Label(form_frame, text="Gender").grid(row=0, column=4, padx=5, pady=5, sticky="e")
        gender_combo = ttk.Combobox(form_frame, textvariable=self.gender_var, values=["Male", "Female"], state="readonly", width=17)
        gender_combo.grid(row=0, column=5, padx=5, pady=5, sticky="w")

        # Row 1
        tk.Label(form_frame, text="First Name").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        tk.Entry(form_frame, textvariable=self.fname_var).grid(row=1, column=1, padx=5, pady=5, sticky="w")

        tk.Label(form_frame, text="Last Name").grid(row=1, column=2, padx=5, pady=5, sticky="e")
        tk.Entry(form_frame, textvariable=self.lname_var).grid(row=1, column=3, padx=5, pady=5, sticky="w")

        tk.Label(form_frame, text="Grade").grid(row=1, column=4, padx=5, pady=5, sticky="e")
        tk.Entry(form_frame, textvariable=self.grade_var).grid(row=1, column=5, padx=5, pady=5, sticky="w")

        # Row 2
        tk.Label(form_frame, text="Email").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        tk.Entry(form_frame, textvariable=self.email_var, width=40).grid(row=2, column=1, columnspan=3, padx=5, pady=5, sticky="w")

        # Buttons
        btn_frame = tk.Frame(root, padx=10, pady=10)
        btn_frame.pack(fill="x")

        tk.Button(btn_frame, text="Add Student", command=self.add_student, bg="#4CAF50", fg="white", width=12).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Update", command=self.update_student, bg="#2196F3", fg="white", width=12).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Delete", command=self.delete_student, bg="#f44336", fg="white", width=12).pack(side="left", padx=5)
        
        # NEW BUTTON HERE
        tk.Button(btn_frame, text="Search by ID", command=self.search_student, bg="#FF9800", fg="white", width=12).pack(side="left", padx=5)
        
        tk.Button(btn_frame, text="Clear Form", command=self.clear_fields, width=10).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Refresh List", command=self.load_students, width=10).pack(side="left", padx=5)

        # Treeview Frame
        tree_frame = tk.Frame(root)
        tree_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Scrollbar
        scrollbar = ttk.Scrollbar(tree_frame)
        scrollbar.pack(side="right", fill="y")

        columns = ("StudentID", "FirstName", "LastName", "Age", "Gender", "Grade", "Email")
        self.tree = ttk.Treeview(tree_frame, columns=columns, show="headings", yscrollcommand=scrollbar.set)
        
        # Configure headings and column widths
        self.tree.heading("StudentID", text="ID")
        self.tree.column("StudentID", width=50, anchor="center")
        
        self.tree.heading("FirstName", text="First Name")
        self.tree.column("FirstName", width=100)
        
        self.tree.heading("LastName", text="Last Name")
        self.tree.column("LastName", width=100)
        
        self.tree.heading("Age", text="Age")
        self.tree.column("Age", width=50, anchor="center")
        
        self.tree.heading("Gender", text="Gender")
        self.tree.column("Gender", width=80, anchor="center")
        
        self.tree.heading("Grade", text="Grade")
        self.tree.column("Grade", width=50, anchor="center")
        
        self.tree.heading("Email", text="Email")
        self.tree.column("Email", width=200)

        self.tree.pack(fill="both", expand=True)
        scrollbar.config(command=self.tree.yview)
        
        self.tree.bind("<ButtonRelease-1>", self.select_student)

        self.load_students()

    # Add Student
    def add_student(self):
        if self.id_var.get() == "" or self.fname_var.get() == "":
            messagebox.showerror("Error", "ID and First Name are required!")
            return
            
        # Check for duplicate ID
        with open(CSV_FILE, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                if row and row[0] == self.id_var.get():
                    messagebox.showerror("Error", "Student ID already exists!")
                    return

        with open(CSV_FILE, "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([
                self.id_var.get(), 
                self.fname_var.get(), 
                self.lname_var.get(), 
                self.age_var.get(),
                self.gender_var.get(), 
                self.grade_var.get(),
                self.email_var.get()
            ])
        self.load_students()
        self.clear_fields()
        messagebox.showinfo("Success", "Student added successfully!")

    # Load students from CSV
    def load_students(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        
        if os.path.exists(CSV_FILE):
            with open(CSV_FILE, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.tree.insert("", "end", values=(
                        row["StudentID"], 
                        row["FirstName"], 
                        row["LastName"], 
                        row["Age"], 
                        row["Gender"], 
                        row["Grade"],
                        row["Email"]
                    ))

    # Search Student by ID
    def search_student(self):
        search_id = self.id_var.get().strip()
        if not search_id:
            messagebox.showwarning("Warning", "Please enter a Student ID to search.")
            return

        found = False
        # Clear current treeview
        for row in self.tree.get_children():
            self.tree.delete(row)

        if os.path.exists(CSV_FILE):
            with open(CSV_FILE, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row["StudentID"] == search_id:
                        # Insert into treeview
                        self.tree.insert("", "end", values=(
                            row["StudentID"], 
                            row["FirstName"], 
                            row["LastName"], 
                            row["Age"], 
                            row["Gender"], 
                            row["Grade"],
                            row["Email"]
                        ))
                        # Populate fields
                        self.fname_var.set(row["FirstName"])
                        self.lname_var.set(row["LastName"])
                        self.age_var.set(row["Age"])
                        self.gender_var.set(row["Gender"])
                        self.grade_var.set(row["Grade"])
                        self.email_var.set(row["Email"])
                        found = True
                        break # Stop after finding the student

        if not found:
            messagebox.showinfo("Result", "No student found with that ID.")
            self.load_students() # Reload full list if not found
        else:
            pass # The list is now filtered to show the found student

    # Clear form fields
    def clear_fields(self):
        self.id_var.set("")
        self.fname_var.set("")
        self.lname_var.set("")
        self.age_var.set("")
        self.gender_var.set("")
        self.grade_var.set("")
        self.email_var.set("")

    # Select student from tree
    def select_student(self, event):
        selected = self.tree.focus()
        if selected:
            values = self.tree.item(selected, "values")
            if values:
                self.id_var.set(values[0])
                self.fname_var.set(values[1])
                self.lname_var.set(values[2])
                self.age_var.set(values[3])
                self.gender_var.set(values[4])
                self.grade_var.set(values[5])
                self.email_var.set(values[6])

    # Update student
    def update_student(self):
        selected = self.tree.focus()
        if not selected:
            messagebox.showerror("Error", "No student selected")
            return
        
        current_id = self.tree.item(selected, "values")[0]
        
        # Read all data
        rows = []
        with open(CSV_FILE, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            rows = list(reader)
            
        # Find and update
        found = False
        for i in range(1, len(rows)): # Skip header
            if rows[i][0] == current_id:
                rows[i] = [
                    self.id_var.get(), 
                    self.fname_var.get(), 
                    self.lname_var.get(), 
                    self.age_var.get(),
                    self.gender_var.get(), 
                    self.grade_var.get(),
                    self.email_var.get()
                ]
                found = True
                break
        
        if found:
            with open(CSV_FILE, "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerows(rows)
            self.load_students()
            self.clear_fields()
            messagebox.showinfo("Success", "Student updated successfully!")
        else:
            messagebox.showerror("Error", "Could not find student ID to update.")

    # Delete student
    def delete_student(self):
        selected = self.tree.focus()
        if not selected:
            messagebox.showerror("Error", "No student selected")
            return
            
        student_id = self.tree.item(selected, "values")[0]
        confirm = messagebox.askyesno("Confirm", f"Are you sure you want to delete student ID {student_id}?")
        if not confirm:
            return

        rows = []
        with open(CSV_FILE, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            rows = list(reader)
            
        # Filter out the student
        new_rows = [rows[0]] # Keep header
        for row in rows[1:]:
            if row[0] != student_id:
                new_rows.append(row)
                
        with open(CSV_FILE, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows(new_rows)
            
        self.load_students()
        self.clear_fields()
        messagebox.showinfo("Success", "Student deleted successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentRecordsApp(root)
    root.mainloop()