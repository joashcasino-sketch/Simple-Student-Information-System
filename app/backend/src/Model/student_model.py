import csv
from os import read
from pathlib import Path

student_csv = Path(__file__).resolve().parent.parent.parent / 'data' / 'students.csv'
class StudentModel:
    def __init__(self):
        self.csv_file = student_csv
        self.headers = ['ID Number', 'Name', 'Gender', 'Year Level', 'Program', 'College']

    def add_student(self, student_data):
        try:
            if self.student_exist(student_data.get('ID Number')):
                return False
            
            with open(self.csv_file, 'a', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=self.headers)
                writer.writerow(student_data)

                return True
            
        except Exception as e:
            print(f"Error adding students: {e}")
            return False
        
    def student_exist(self, student_id):
        try:
            with open(self.csv_file, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row['ID Number'] == student_id:
                        return True
            return False
        except FileNotFoundError:
            return False
        
    def edit_student(self, student_data):
        try:
            rows = []
            found = False

            with open(self.csv_file, 'r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row["ID Number"] == student_data.get("ID Number"):
                        rows.append(student_data)
                        found = True
                    else:
                        rows.append(rows)

            if not found:
                return False
            
            with open(self.csv_file, 'a', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=self.headers)
                writer.writeheader()
                writer.writerow(rows)

            return True

        except Exception as e:
            print(f"Error update student: {e}")
            return False

    def delete_student(self, student_id):
        try:
            rows = []
            found = False

            with open(self.csv_file, 'r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row['ID Number'] == student_id:
                        found = True
                    else:
                        rows.append(row)
            
            if not found:
                return False

            with open(self.csv_file, 'w', newline='', encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames=self.headers)
                writer.writeheader()
                writer.writerows(rows)

            return True
    
        except Exception as e:
            print(f"Error deleting student {e}")
            return False