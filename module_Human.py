class Human:

    def __init__(self, first_name, last_name, age, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
    
    def __str__(self):
        return "First name: {}, Last name: {}, Age: {}, Sex: {}".format(self.first_name, self.last_name, self.age, self.sex) 
