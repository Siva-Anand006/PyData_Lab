'''
The exercise template includes a class named ExamSubmission, which models an examinee's submission in an exam. 
The ExamSubmission class has the following attributes:

examinee (str): The name of the examinee.
points (int): The score obtained by the examinee.
Your task is to write a function named passed(submissions: list, lowest_passing: int), which takes two arguments:

submissions: A list of ExamSubmission objects.
lowest_passing: An integer representing the lowest passing grade.
The function should return a new list containing only the ExamSubmission objects from the original 
list that meet or exceed the lowest_passing grade. You are not allowed to modify the original list 
of submissions or the ExamSubmission class definition.

'''
class ExamSubmission:
    
    def __init__(self, examinee: str, points: int ):
        self.examinee = examinee
        self.points = points
    
def passed(submissions: list, lowest_passing: int) -> list :
    passed_list = []
    for submission in submissions:
        if submission.points >= lowest_passing:
            passed_list.append(submission)
    
    return passed_list
    
if __name__ == "__main__":
    s1 = ExamSubmission("Peter", 12)
    s2 = ExamSubmission("Pippa", 19)
    s3 = ExamSubmission("Paul", 15)
    s4 = ExamSubmission("Phoebe", 9)
    s5 = ExamSubmission("Persephone", 17)

    passes = passed([s1, s2, s3, s4, s5], 15)
    for passing in passes:
        print(passing.examinee)
