# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   GMcCaslin,2/24/2025,Created Script
#   <Your Name Here>,<Date>, <Activity>
# ------------------------------------------------------------------------------------------ #
from fileinput import close

#import json library
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Changed this from csv to json
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
#student_data: list=[]
student_data: dict= {}  # one row of student data (TODO: Change this to a Dictionary)
students: list = []  # a table of student data
#csv_data: str = ''  # Holds combined CSV data. Note: Remove later since it is NOT needed with the JSON File
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.


# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
try:
    file = open(FILE_NAME, "r")
    #for row in file.readlines():
        # Transform the data from the file
        #student_data = row.split(',')
        #student_data = [student_data[0], student_data[1], student_data[2].strip()]
        # Load it into our collection (list of lists)
        #students.append(student_data)
    students=json.load(file)
    #file.close()
except FileNotFoundError as e:
        print("This file doesn't exist")
except Exception as e:
        print("There was an error opening the file")
        print(e, e.__doc__)
finally:
        print("Closing file")
        file.close()

# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                    raise ValueError('The first name can only be letter characters')
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                    raise ValueError('The last name can only be letter characters')
            course_name = input("Please enter the name of the course: ")
            student_data = {"FirstName":student_first_name,"LastName":student_last_name,"CourseName":course_name}#dictionary
            students.append(student_data)#dictionary to the list
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            print("User entered invalid value. Continuing...")
        continue #Moved the continue line above the print



    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        #print("-"*50)
        #for student in students:
        #    print(f"Student {student[0]} {student[1]} is enrolled in {student[2]}")
        #print("-"*50)
        for student in students:
            print(student["FirstName"],student["LastName"],student["CourseName"])
        continue

    # Save the data to a file
    elif menu_choice == "3":
        #file = open(FILE_NAME, "w")
        #for student in students:
        #    csv_data = f"{student[0]},{student[1]},{student[2]}\n"
        #    file.write(csv_data)
        #file.close()
        #file=open('data.json','w')
        try:
            file=open(FILE_NAME,'w')
            json.dump(students,file)
        except Exception as e:
            print("There was an error writing the file")
            print(e, e.__doc__)
        finally:
            print("Closing file")
            file.close()
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
