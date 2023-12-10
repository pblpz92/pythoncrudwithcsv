import csv

class FileManager:

    def __init__(self, file_name):
        self.file_name = file_name
        self.courses_list = self.read_courses()  # Load the courses in the csv at start

    def read_courses(self):
        courses = []
        with open(self.file_name, mode='r', newline='') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header line

            for line in reader:
                courses.append(line)
        return courses

    def search_course(self, course_id):
        for course in self.courses_list:
            if course[0] == str(course_id):
                return course
        return None

    def delete_course(self, course_id): #Instead deleting mark as not visible
        for course in self.courses_list:
            if course[0] == str(course_id):
                course[6] = 'False'
        self.update_csv_file()

    def modify_course(self, modified_course):
        for course in self.courses_list:
            if course[0] == str(modified_course.course_id):
                course[1] = modified_course.hours
                course[2] = modified_course.remote
                course[3] = modified_course.course_name
                course[4] = modified_course.course_teacher
                course[5] = modified_course.course_area
                course[6] = modified_course.visible
        self.update_csv_file()

    def update_csv_file(self):
        with open(self.file_name, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Hours", "Remote", "Course Name", "Course Teacher", "Course Area", "Visible"])

            for course in self.courses_list:
                writer.writerow(course)

    def update_csv_file_gui(self, courses_to_add):
        with open(self.file_name, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Hours", "Remote", "Course Name", "Course Teacher", "Course Area", "Visible"])

            for course in courses_to_add:
                writer.writerow(course)

    def update_erased_courses(self, courses_to_add):
        erased_courses = []
        for curso in courses_to_add:
            if curso[6] == 'False':
                erased_courses.append(curso)
        print(erased_courses)
        with open('files/erased_courses.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Hours", "Remote", "Course Name", "Course Teacher", "Course Area", "Visible"])

            for course in erased_courses:
                writer.writerow(course)




#if __name__ == "__main__":
#    file_manager = FileManager('files/courses.csv')
#    file_manager.delete_course(2)
