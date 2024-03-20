class student:
    def __init__(self, name, studentId):
        self.name = name
        try:
            self.studentId = int(studentId)
        except ValueError:
            print(f"Error: Student ID for '{name}' must be an integer. Received: '{studentId}'. ID set to None.")
            self.studentId = None
        
    def whoami(self):
        if self.studentId is not None:
            print(f'Student ID: {self.studentId}, Student Name: {self.name}\n')
        else:
            print(f"Student Name: {self.name}. No valid ID provided.\n")
