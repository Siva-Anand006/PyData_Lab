"""
Create a class named CompletedCourse that represents a university course
a student has completed. Each course should have the following attributes:

course_name (a string representing the name of the course)
credits (an integer representing the number of credits for the course)
completion_date (a date object representing the date when the course was completed)
Once you have created the class, perform the following tasks:

Create a list to store completed courses.
Instantiate at least four CompletedCourse objects with different course names, credit values, and completion dates.
Add these objects to your list of completed courses.
Loop through the list and print out the name of each completed course.
Calculate the total number of credits received for all completed courses and print the result.

"""

from datetime import date

class CompletedCourse:
    
    def __init__( self,course_name: str, credits:int, completion_date :date ):
        self.course_name = course_name
        self.credits = credits
        self.completion_date = completion_date
    

if __name__ == "__main__":
    
    completed = []
    
    maths1 = CompletedCourse("Mathematics 1", 5, date(2020, 3, 11))
    prog1 = CompletedCourse("Programming 1", 6, date(2019, 12, 17))
    Political_Science_1 = CompletedCourse("Political Science 1", 5, date(2020, 4, 12))
    History_1 = CompletedCourse("History 1", 6, date(2019, 11, 27))
    
    completed.append(maths1)
    completed.append(prog1)
    completed.append(Political_Science_1)
    completed.append(History_1)
    
    credits = 0
    for course in completed:
        print(course.course_name)
        credits += course.credits
    print(f"Total credits {credits}")
    
    
    