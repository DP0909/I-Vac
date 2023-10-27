import tkinter as tk
import mysql.connector

# Establish a connection to your MySQL database
conn = mysql.connector.connect(
    host="127.0.0.1",  # Replace with your MySQL server host
    user="root",  # Replace with your MySQL username
    password="Deep@2001",  # Replace with your MySQL password
    database="employee",  # Replace with the name of your MySQL database
)


def generate_employee_id():
    name = name_entry.get()
    department = department_entry.get()

    # Your logic to generate the ID
    employee_id = name[:3].upper() + department[:2].upper() + "001"

    # Display the generated ID
    id_label.config(text=f"Employee ID: {employee_id}")

    # Store the ID in the database
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO employees (name, department, employee_id) VALUES (%s, %s, %s)",
        (name, department, employee_id),
    )
    conn.commit()
    cursor.close()


# Create the GUI
window = tk.Tk()
window.title("Employee ID Generator")

name_label = tk.Label(window, text="Name:")
name_label.pack()

name_entry = tk.Entry(window)
name_entry.pack()

department_label = tk.Label(window, text="Department:")
department_label.pack()

department_entry = tk.Entry(window)
department_entry.pack()

generate_button = tk.Button(window, text="Generate ID", command=generate_employee_id)
generate_button.pack()

id_label = tk.Label(window, text="")
id_label.pack()

window.mainloop()
