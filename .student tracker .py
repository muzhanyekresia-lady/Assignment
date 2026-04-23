#  stident_score_tracker.

import json
import os

FILE_NAME = "students.json"

# Load records from file
def load_records():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            try:
                return json.load(file)
            except:
                return {}
    return {}

# Save records to file
def save_records(records):
    with open(FILE_NAME, "w") as file:
        json.dump(records, file)

# Add student
def add_student(records):
    name = input("Enter student name: ")
    if name in records:
        print("Student already exists!")
        return
    score = float(input("Enter score: "))
    records[name] = score
    print("Student added successfully.")

# View students
def view_students(records):
    if not records:
        print("No records found.")
        return
    print("\n--- Student Scores ---")
    for name, score in records.items():
        print(f"{name}: {score}")

# Update score
def update_student(records):
    name = input("Enter student name to update: ")
    if name not in records:
        print("Student not found.")
        return
    score = float(input("Enter new score: "))
    records[name] = score
    print("Score updated successfully.")

# Delete student
def delete_student(records):
    name = input("Enter student name to delete: ")
    if name in records:
        del records[name]
        print("Student deleted.")
    else:
        print("Student not found.")

# Calculate statistics
def calculate_statistics(records):
    if not records:
        print("No data available.")
        return
    scores = list(records.values())
    avg = sum(scores) / len(scores)
    print("\n--- Statistics ---")
    print(f"Average Score: {avg:.2f}")
    print(f"Highest Score: {max(scores)}")
    print(f"Lowest Score: {min(scores)}")

# Main program
def main():
    records = load_records()

    while True:
        print("\n===== Student Score Tracker =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Score")
        print("4. Delete Student")
        print("5. Calculate Statistics")
        print("6. Save Records")
        print("7. Exit")

        choice = input("Enter choice (1-7): ")

        if choice == "1":
            add_student(records)
        elif choice == "2":
            view_students(records)
        elif choice == "3":
            update_student(records)
        elif choice == "4":
            delete_student(records)
        elif choice == "5":
            calculate_statistics(records)
        elif choice == "6":
            save_records(records)
            print("Records saved.")
        elif choice == "7":
            save_records(records)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()