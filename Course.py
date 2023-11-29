class Course:
    def __init__(self, course_id, hours, remote, course_name, course_teacher, course_area):
        self.course_id = course_id
        self.hours = hours
        self.remote = remote
        self.course_name = course_name
        self.course_teacher = course_teacher
        self.course_area = course_area
        self.visible = True

    def __str__(self):
        return f"ID: {self.course_id}, Course name: {self.course_name}, hours: {self.hours}, Remote: {self.remote}, teacher: {self.course_teacher}, topic: {self.course_area}, Visible: {self.visible}"

    def __eq__(self, other_course):
        if not isinstance(other_course, Course):
            return False
        return self.course_id == other_course.course_id

    def get_headers(cls):
        return ['id', 'hours', 'remote', 'course_name', 'course_teacher', 'course_area', 'visible']


""" little testing
if __name__ == "__main__":
    test_course = Course(1, 30, True, "Python Basics", "John Doe", "Programming")
    print("Información del curso creado:")
    print(test_course)
"""