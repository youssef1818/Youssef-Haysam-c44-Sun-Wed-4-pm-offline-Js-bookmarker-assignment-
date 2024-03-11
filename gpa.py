def gpa_calc():
    # This function does the actual calculation of GPA
    def gpa_real_calc(grade_if):
        result = 0
        if grade_if == "F":
            result = 0
        elif grade_if == "D-":
            result = 1
        elif grade_if == "D":
            result = 1.5
        elif grade_if == "D+":
            result = 2
        elif grade_if == "C-":
            result = 2.2
        elif grade_if == "C":
            result = 2.4
        elif grade_if == "C+":
            result = 2.6
        elif grade_if == "B-":
            result = 2.8
        elif grade_if == "B":
            result = 3
        elif grade_if == "B+":
            result = 3.2
        elif grade_if == "A-":
            result = 3.4
        elif grade_if == "A":
            result = 3.7
        elif grade_if == "A+":
            result = 4

        return result

    # This function converts marks to letter grades
    def gpa_mark_to_grade(mark_if):
        if mark_if < 50:
            result = "F"
        elif mark_if < 55:
            result = "D-"
        elif mark_if < 60:
            result = "D"
        elif mark_if < 64:
            result = "D+"
        elif mark_if < 68:
            result = "C-"
        elif mark_if < 72:
            result = "C"
        elif mark_if < 76:
            result = "C+"
        elif mark_if < 80:
            result = "B-"
        elif mark_if < 84:
            result = "B"
        elif mark_if < 88:
            result = "B+"
        elif mark_if < 92:
            result = "A-"
        elif mark_if < 96:
            result = "A"
        else:
            result = "A+"

        return result

    grade_list = ["F", "D-", "D", "D+", "C-", "C", "C+",
                  "B-", "B", "B+", "A-", "A", "A+"]

    while True:
        subject_grade = []
        subject_hour = []
        gpa_sum = 0
        gpa_hour = 0

        # Here starts the menu
        print("=================================\n"
              "=== Welcome To GPA Calculator ===\n"
              "=================================")

        # Here user has a choice between letter grades (A+, B-, ...) or numerical marks (86, 15, 46, ...)
        choice_1 = input("Do you want to use:\n"
                         "1) Grades\n"
                         "2) Marks\n")

        while choice_1 != "1" and choice_1 != "2":
            choice_1 = input("Please enter a valid choice: ")

        # Taking the number of subjects
        subjects = input("How many subjects do you have? ")

        while str.isdigit(subjects) is False or int(subjects) < 1:
            subjects = input("Please enter a valid number of subjects: ")

        # A loop for setting the (1st, 2nd, 3th, 4th, ...)
        # and for calculating the GPA
        for i in range(1, int(subjects) + 1):
            if i == 1:
                rate = "1st"
            elif i == 2:
                rate = "2nd"
            elif i == 3:
                rate = "3rd"
            else:
                rate = f"{i}th"

            # Taking each subject's grade or mark depending on the user choose
            if choice_1 == "1":
                grade = str.capitalize(input(f"Enter {rate} Subject grade: "))
                while grade not in grade_list:
                    grade = str.capitalize(input(f"Grade must be from {grade_list}\n"
                                                 f"enter again: "))
                subject_grade.append(grade)

            else:
                mark = input(f"Enter {rate} Subject mark: ")
                while str.isdigit(mark) is False or int(mark) < 0 or int(mark) > 100:
                    mark = input("Marks must be from 0 - 100, enter again: ")

                subject_grade.append(gpa_mark_to_grade(int(mark)))

            # Taking each subject's hours
            hour = input(f"Enter {rate} Subject hours: ")
            while str.isdigit(hour) is False or int(hour) < 0:
                hour = input("Please enter a valid number of hours: ")
            subject_hour.append(int(hour))

            # Actual GPA calculation after collecting info
            gpa_sum += gpa_real_calc(subject_grade[i-1]) * subject_hour[i-1]
            gpa_hour += subject_hour[i-1]

        gpa = gpa_sum / gpa_hour
        print(f"Your GPA is {gpa}")

        choice_2 = input("Do you want to calculate again?\n"
                         "1) Calculate again\n"
                         "2) Exit Program\n")

        while choice_2 != "1" and choice_2 != "2":
            choice_2 = input("Please enter a valid choice: ")

        if choice_2 == "2":
            print("Bye-bye!")
            exit()

gpa_calc()