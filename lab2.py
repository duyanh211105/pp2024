class Person:
    def __init__(self, person_id, name, dob):
        self.id = person_id
        self.name = name
        self.dob = dob

    def input(self):
        self.id = input("Enter ID: ")
        self.name = input("Enter Name: ")
        self.dob = input("Enter Date of Birth (DD/MM/YYYY): ")

    def display(self):
        return f"ID: {self.id}, Name: {self.name}, DOB: {self.dob}"


class Student(Person):
    def __init__(self, student_id="", name="", dob=""):
        super().__init__(student_id, name, dob)
        self.marks = {}

    def add_mark(self, course_id, mark):
        self.marks[course_id] = mark

    def get_mark(self, course_id):
        return self.marks.get(course_id, "N/A")


class Course:
    def __init__(self, course_id, name):
        self.id = course_id
        self.name = name

    def input(self):
        self.id = input("Enter Course ID: ")
        self.name = input("Enter Course Name: ")

    def display(self):
        return f"ID: {self.id}, Name: {self.name}"


class StudentMarkManagementSystem:
    def __init__(self):
        self.students = []
        self.courses = []

    def input_students(self):
        num_students = int(input("Enter the number of students: "))
        for _ in range(num_students):
            student = Student()
            print("\n--- Enter Student Information ---")
            student.input()
            self.students.append(student)

    def input_courses(self):
        num_courses = int(input("Enter the number of courses: "))
        for _ in range(num_courses):
            course = Course("", "")
            print("\n--- Enter Course Information ---")
            course.input()
            self.courses.append(course)

    def input_marks_for_course(self):
        course_id = input("\nEnter the Course ID to input marks: ")
        course = next((c for c in self.courses if c.id == course_id), None)
        if not course:
            print("Course not found!")
            return

        print(f"\n--- Inputting Marks for {course.name} ---")
        for student in self.students:
            mark = float(input(f"Enter marks for {student.name} (ID: {student.id}): "))
            student.add_mark(course_id, mark)

    def list_courses(self):
        print("\n--- List of Courses ---")
        for course in self.courses:
            print(course.display())

    def list_students(self):
        print("\n--- List of Students ---")
        for student in self.students:
            print(student.display())

    def show_student_marks(self):
        course_id = input("\nEnter the Course ID to view marks: ")
        course = next((c for c in self.courses if c.id == course_id), None)
        if not course:
            print("Course not found!")
            return

        print(f"\n--- Marks for {course.name} ---")
        for student in self.students:
            mark = student.get_mark(course_id)
            print(f"{student.name} (ID: {student.id}): {mark}")


def main():
    system = StudentMarkManagementSystem()
    while True:
        print("\n--- Student Mark Management System ---")
        print("1. Input student information")
        print("2. Input course information")
        print("3. Input marks for a course")
        print("4. List courses")
        print("5. List students")
        print("6. Show student marks for a course")
        print("7. Exit")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                system.input_students()
            elif choice == 2:
                system.input_courses()
            elif choice == 3:
                system.input_marks_for_course()
            elif choice == 4:
                system.list_courses()
            elif choice == 5:
                system.list_students()
            elif choice == 6:
                system.show_student_marks()
            elif choice == 7:
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid choice! Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    main()
