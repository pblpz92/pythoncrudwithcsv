import csv

class FileManager:

    def __init__(self, file_name):
        self.file_name = file_name
        self.courses_list = self.read_courses()

    def read_courses(self):
        courses = []

        with open(self.file_name, mode='r', newline='') as file:
            reader = csv.reader(file)
            next(reader)

            for line in reader:
                courses.append(line)

        return courses

    def search_course(self, course_id):
        for course in self.courses_list:
            if course[0] == str(course_id):
                return course
        return None

    def delete_course(self, course_id):
        for course in self.courses_list:
            if course[0] == str(course_id):
                course[6] = 'False'
        self.update_csv_file()

    def update_csv_file(self):
        with open(self.file_name, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Hours", "Remote", "Course Name", "Course Teacher", "Course Area", "Erased"])

            for course in self.courses_list:
                writer.writerow(course)



if __name__ == "__main__":
    file_manager = FileManager('files/courses.csv')
    file_manager.delete_course(2)



