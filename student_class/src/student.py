class Student:
    def __init__(self, input_name, input_cohort):
        self.name = input_name
        self.cohort = input_cohort
        
    def student_has_name(self):
            return self.name

    def student_has_cohort(self):
            return self.cohort

    def talk(self):
            return "I can talk!"

    def say_favourite_language(self, language):
            return f"I love {language}"