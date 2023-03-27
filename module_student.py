import module_Human as m_h
class Student(m_h.Human):

    def __init__(self, first_name, last_name, age, sex, faculty, group):
        super().__init__(first_name, last_name, age, sex)
        self.faculty = faculty
        self.group = group

    def __str__(self):
        return "Student: " + super().__str__() + ", Faculty = {}, Group = {}".format(self.faculty, self.group)
        