import math

def facrorial(n):
    k = 1
    while n >= 2:
        k *= n
        n  -= 1
    return k

def square_roots(n : list):
    return [ math.sqrt(x) for x in n]

def rows_of_stars(n: list):
    return ['*' * int(number) for number in n]

class ExamResult:
    def __init__(self, name : str , sub1 : int, sub2 : int, sub3 : int):
        self.name = name
        self.sub1 = sub1
        self.sub2= sub2
        self.sub3= sub3
        self.highest = max(self.sub1,self.sub2,self.sub3)
        

def best_results(results : list):
    return [x.highest for x in results]
    


if __name__ == "__main__":
    numbers = [x for x in range(1,10)]
    
    factorials = [ facrorial(number) for number in numbers]
    
    print(numbers)
    print(factorials)

    lines = square_roots([1,2,3,4])
    
    for line in lines:
        print(line)
        
        
    rows = rows_of_stars([1,2,3,4])
    for row in rows:
        print(row)

    print()

    rows = rows_of_stars([4, 3, 2, 1, 10])
    for row in rows:
        print(row)
        
    result1 = ExamResult("Peter",5,3,4)
    result2 = ExamResult("Pippa",3,4,1)
    result3 = ExamResult("Paul",2,1,3)
    results = [result1, result2, result3]
    print(best_results(results))