import module_Human as m_h
import module_student as stud
import module_Group as m_g

# create student

student1 = stud.Student("Vlad", "Petrenko", 17, "men","Economics", 53)
student2 = stud.Student("Andrey", "Shevchenko", 16, "men", "Economics", 53 )
student3 = stud.Student("Anna", "Kurnikova", 16, "woomen", "Economics", 53)
student4 = stud.Student("Oleg", "Pivovarov", 17, "men","Economics", 53)
student5 = stud.Student("Andrey", "Kurnikov", 16, "men", "Economics", 53 )
student6 = stud.Student("Svetlana", "Kurnikova", 16, "woomen", "Economics", 53)
student7 = stud.Student("Vladimir", "Pevcov", 17, "men","Economics", 53)
student8 = stud.Student("Anna", "Shevchenko", 16, "men", "Economics", 53 )
student9 = stud.Student("Annastasiya", "Kotelnikova", 16, "woomen", "Economics", 53)
student10 = stud.Student("Anna", "Ciplenkova", 16, "woomen", "Economics", 53)
student11 = stud.Student("Alina", "Kovalenko", 18, "woomen", "Economics", 53)


group_53 = m_g.Group()

group_53.add_student(student1)
group_53.add_student(student2)
group_53.add_student(student3)
group_53.add_student(student4)
group_53.add_student(student5)
group_53.add_student(student6)
group_53.add_student(student7)
group_53.add_student(student8)
group_53.add_student(student9)
group_53.add_student(student10)
group_53.add_student(student11)




print(group_53)
print(group_53.search_student("Shevchenko"))
