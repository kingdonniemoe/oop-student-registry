import re

class Student:
    count = 1

    def __init__(self, name, age=13, grade="12th"):
        self._name = name
        self._age = int(age)
        self._grade = grade
        self.student_count = Student.count
        Student.count += 1

    @property
    def get_name(self):
        return self._name
    
    @get_name.setter
    def set_name(self, name):
        try:
            if re.match(r'^[A-Z][a-zA-Z]{2,}$', name):
                self._name = name
            else:
                raise ValueError("Invalid Name")
            
        except TypeError:
            print("Invaled input type for name. Name not updated.")

    @property
    def get_age(self):
        return self._age
    
    @get_age.setter
    def set_age(self, age):
        try: 
            if type(age) == int and age > 11 and age < 18:
                self._age = int(age)
        except:
            if type(age) != int:
                raise TypeError("Must be an integer")
            
            elif age < 11:
                raise ValueError("You are too young!")
            
            elif age > 18:
                raise ValueError("You are too old!")
            
    @property
    def get_grade(self):
        return self._grade
    
    @get_grade.setter
    def set_grade(self, grade):
        try:
            if re.match(r'(9|10|11|12)th$', grade):
                self._grade = grade
        except:
            match = re.match(r'^(\d+)', grade)

            if int(match.group(1)) > 12:
                raise ValueError("You already passed these grades")
            
            elif int(match.group(1)) < 9:
                raise ValueError("Not quite there yet, keep living.")

    def __str__(self):
        return f"Student {self.student_count}: Name: {self._name}, Age: {self._age}, Grade: {self._grade}"
    
    def advance(self):
        grade = self.get_grade()
        match = re.match(r'^(\d+)', grade)
        self._grade = str(int(match.group(1)) + 1) +'th'
        return f'{self._name} has advanced to the {self._grade} grade.'

    def study(self, subject):
        return f'{self._name} is studying {subject}'
