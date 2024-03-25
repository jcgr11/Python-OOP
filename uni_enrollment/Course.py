from exceptions import AlreadyEnrolledError, CapacityReachedError, StudentNotFoundError


class course:
    def __init__(self, className, studentCapacity, waitlistCapacity):
        self.className = className
        self.studentCapacity = studentCapacity
        self.waitlistCapacity = waitlistCapacity
        self.myStudents = []
        self.waitlist = []
        self.numStudents = len(self.myStudents)

    def enrollStudent(self, student_obj):
        if student_obj in self.myStudents:
            raise AlreadyEnrolledError(f"Error:{student_obj.name} already enrolled")
        elif len(self.myStudents) >= self.studentCapacity:
            if len(self.waitlist) >= self.waitlistCapacity:
                raise CapacityReachedError(
                    f"Error: Waitlist and Class are full. Cannot enroll {student_obj.name}."
                )
            else:
                self.waitlist.append(student_obj)
                print(f"Class at capacity. {student_obj.name} has been waitlisted.")
        else:
            self.myStudents.append(student_obj)
            self.numStudents = len(self.myStudents)
            print(f"{student_obj.name} has been enrolled!")

    def dropStudent(self, name):
        for student in self.myStudents:
            if student.name == name:
                self.myStudents.remove(student)
                self.numStudents = len(self.myStudents)
                print(f"{name} has dropped the course.")

                if self.waitlist and len(self.myStudents) < self.studentCapacity:
                    newStudent = self.waitlist.pop(0)
                    self.enrollStudent(newStudent)
                return
        raise StudentNotFoundError(f"Error: Student, {name}, is not currently enrolled")

    def printEnrolled(self):
        print("\nEnrolled:")
        for student in self.myStudents:
            print(f"{student.name}, ({student.studentId})")

    def printWaitlisted(self):
        print("\nWaitlisted:")
        for student in self.waitlist:
            print(f"{student.name}, ({student.studentId})")
