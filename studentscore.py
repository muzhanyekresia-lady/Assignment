import json
import os

FILE_NAME = "students.json"

def add_student(records):
    name = input("Enter student name: ")
    if name in records:
        print("Student already exists!")
        return
    score = float(input("Enter score: "))
    records[name] = score
    print("Student added successfully.")

    
def view_students(records):
    if not records:
        print("No records found.")
        return
    print("\n--- Student Scores ---")
    for name, score in records.items():
        print(f"{name}: {score}")


def update_student(records):
    name = input("Enter student name to update: ")
    if name not in records:
        print("Student not found.")
        return
    score = float(input("Enter new score: "))
    records[name] = score
    print("Score updated successfully.")


def delete_student(records):
    name = input("Enter student name to delete: ")
    if name in records:
        del records[name]
        print("Student deleted.")
    else:
        print("Student not found.")


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


def load_records():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            try:
                return json.load(file)
            except:
                return {}
    return {}


def save_records(records):
    with open(FILE_NAME, "w") as file:
        json.dump(records, file)


def main():
    records = load_records()

    while True:
        print("\n===== Student Score Tracker =====")
        print("A. Add Student")
        print("B. View Students")
        print("C. Update Score")
        print("D. Delete Student")
        print("E. Calculate Statistics")
        print("F. Save Records")
        print("G. Exit")

        choice = input("Enter choice (1-7): ")

        if choice == "A":
            add_student(records)
        elif choice == "B":
            view_students(records)
        elif choice == "C":
            update_student(records)
        elif choice == "D":
            delete_student(records)
        elif choice == "E":
            calculate_statistics(records)
        elif choice == "F":
            save_records(records)
            print("Records saved.")
        elif choice == "G":
            save_records(records)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()