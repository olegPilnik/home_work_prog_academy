class ExcessNumberError(Exception):

    def __init__(self):
        super().__init__()

    def __str__(self):
        return "The group is complete"


class Group:

    def __init__(self):
        self.list_student = []

    def add_student(self, student):
        try:
            if len(self.list_student) == 10:
                raise ExcessNumberError
            self.list_student.append(student)
        except ExcessNumberError as err:
            print(err)
        

    def del_student(self, student):
        self.list_student.remove(student)

    def search_student(self, last_name):
        for student in self.list_student:
            if student.last_name == last_name:
                print(student)

    def __str__(self):
        result = ''
        for student in self.list_student:
            result += (str(student) + "\n")
        return "Group:\n" + result