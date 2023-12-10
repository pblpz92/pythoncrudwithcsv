import PySimpleGUI as psg

from FileManagement import FileManager

file_manager = FileManager('files/courses.csv')
courses_list = file_manager.read_courses()

def update_or_add_course(new_course_data):
    new_course_id = int(new_course_data[0])
    for index, course in enumerate(courses_list): #Index needed, obtained via enumerate
        if new_course_id == int(course[0]):
            courses_list[index] = new_course_data
            return True  # Found and updated
    courses_list.append(new_course_data)
    return False  # Not found and added

def set_not_visible(course_id):
    for index, course in enumerate(courses_list):
        if ((int(course_id) == int(course[0])) and bool(courses_list[index][6]) == True):
            courses_list[index][6] = False
            return True
    return False

def filter_courses(courses_list):
    visible_courses = []
    for curso in courses_list:
        if curso[6] == 'True':
            visible_courses.append(curso)
    return visible_courses

def display_courses_gui():
    new_course_layout = [
        [psg.Text("Course ID:"), psg.InputText(key='-NewCourseID-')],
        [psg.Text("Course hours:"), psg.InputText(key='-NewCourseHours-')],
        [psg.Text("Course remote:"), psg.InputText(key='-NewCourseRemote-')],
        [psg.Text("Course Name:"), psg.InputText(key='-NewCourseName-')],
        [psg.Text("New Course Teacher:"), psg.InputText(key='-NewCourseTeacher-')],
        [psg.Text("New Course Area:"), psg.InputText(key='-NewCourseArea-')],
        [psg.Button("Add")]
    ]

    layout = [  # Layout structure
        [psg.Text("Courses List")],  # Title
        [psg.Table(values=filter_courses(courses_list),  # Data
                   headings=["ID", "Hours", "Remote", "Course Name", "Course Teacher", "Course Area", "Visible"],
                   auto_size_columns=True,
                   display_row_numbers=False,
                   enable_events=True,
                   enable_click_events=True,
                   key='-Table-')],
        [psg.Column(new_course_layout, key='-NEW_COURSE-')],
        [psg.Button("Delete")],
        [psg.Button("Exit")]
    ]
    window = psg.Window("Courses Information", layout)

    while True:
        event, values = window.read()
        if event == psg.WIN_CLOSED or event == "Exit":  # Click exit button or exit icon
            file_manager.update_erased_courses(courses_list)
            file_manager.update_csv_file_gui(courses_list)
            break

        if event == "Add":
            new_course_id = values['-NewCourseID-']
            new_course_hours = values['-NewCourseHours-']
            new_course_remote = values['-NewCourseRemote-']
            new_course_name = values['-NewCourseName-']
            new_course_teacher = values['-NewCourseTeacher-']
            new_course_area = values['-NewCourseArea-']
            new_course_data = [new_course_id, new_course_hours, new_course_remote, new_course_name, new_course_teacher, new_course_area, True]

            update_or_add_course(new_course_data)
            visible_courses = filter_courses(courses_list)  # Filtering and sending only visible courses
            print(visible_courses)
            window['-Table-'].update(visible_courses)  # Update with new content

            window['-NewCourseID-'].update('')  # Clear input fields
            window['-NewCourseHours-'].update('')
            window['-NewCourseRemote-'].update('')
            window['-NewCourseName-'].update('')
            window['-NewCourseTeacher-'].update('')
            window['-NewCourseArea-'].update('')

        if event == "Delete":
            if selected_course_id is not None:
                set_not_visible(selected_course_id)
                visible_courses = filter_courses(courses_list) #Filtering and sending only visible courses
                window['-Table-'].update(values = visible_courses)  # Update with new content

        if event == "-Table-":
            selected_row = values['-Table-']
            if selected_row:  # Check if a row is selected
                selected_index = selected_row[0]
                selected_data = courses_list[selected_index]
                selected_course_id = selected_data[0]
                print("Selected Row Data:", selected_data)
                print("Selected Row id:", selected_course_id)
    window.close()

if __name__ == "__main__":
    display_courses_gui()