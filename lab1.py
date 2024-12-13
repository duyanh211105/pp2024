def input_num_students():
    return int(input("Enter the number of students: "))


def input_student_info(num_students):
    students = []
    print("\n--- Entering Student Information ---")
    for _ in range(num_students):
        student_id = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        dob = input("Enter Student Date of Birth (DD/MM/YYYY): ")
        students.append({"id": student_id, "name": name, "dob": dob, "marks": {}})
    return students


def input_num_courses():
    return int(input("Enter the number of courses: "))


def input_course_info(num_courses):
    courses = []
    print("\n--- Entering Course Information ---")
    for _ in range(num_courses):
        course_id = input("Enter Course ID: ")
        course_name = input("Enter Course Name: ")
        courses.append({"id": course_id, "name": course_name})
    return courses


def input_marks_for_course(courses, students):
    course_id = input("\nEnter the Course ID to input marks: ")
    course = next((c for c in courses if c["id"] == course_id), None)
    if not course:
        print("Course not found!")
        return

    print(f"\n--- Inputting Marks for {course['name']} ---")
    for student in students:
        mark = float(input(f"Enter marks for {student['name']} (ID: {student['id']}): "))
        student["marks"][course_id] = mark


def list_courses(courses):
    print("\n--- List of Courses ---")
    for course in courses:
        print(f"ID: {course['id']}, Name: {course['name']}")


def list_students(students):
    print("\n--- List of Students ---")
    for student in students:
        print(f"ID: {student['id']}, Name: {student['name']}, DOB: {student['dob']}")


def show_student_marks(courses, students):
    course_id = input("\nEnter the Course ID to view marks: ")
    course = next((c for c in courses if c["id"] == course_id), None)
    if not course:
        print("Course not found!")
        return

    print(f"\n--- Marks for {course['name']} ---")
    for student in students:
        mark = student["marks"].get(course_id, "N/A")
        print(f"{student['name']} (ID: {student['id']}): {mark}")


def main():
    students = []
    courses = []
    while True:
        print("\n--- Student Mark Management System ---")
        print("1. Input number of students")
        print("2. Input student information")
        print("3. Input number of courses")
        print("4. Input course information")
        print("5. Input marks for a course")
        print("6. List courses")
        print("7. List students")
        print("8. Show student marks for a course")
        print("9. Exit")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                num_students = input_num_students()
            elif choice == 2:
                students = input_student_info(num_students)
            elif choice == 3:
                num_courses = input_num_courses()
            elif choice == 4:
                courses = input_course_info(num_courses)
            elif choice == 5:
                input_marks_for_course(courses, students)
            elif choice == 6:
                list_courses(courses)
            elif choice == 7:
                list_students(students)
            elif choice == 8:
                show_student_marks(courses, students)
            elif choice == 9:
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid choice! Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    main()
