# class Student:
#     name = 'Prakhar'
#     roll = 154
#     age = 19
#     branch = 'CSE'
#     # print(name)

# obj = Student()
# print(obj.name)
# class Teacher:
#     name = 'Mohit'
#     id = 176
#     age = 31
#     branch = 'CSE'

# obj2 = Teacher()
# print(obj2.name)

class Student:
    name = 'Prakhar'
    roll = 154
    age = 19
    branch = 'CSE'

    def show_info(self):
        print(self.name)
        print(self.age)

obj1 = Student()
obj2 = Student()

# print(obj1.name)
# print(obj2.name)
obj1.show_info()

# obj1.name = "Sunil"
# print(obj1.name)
# print(obj2.name)

# st_obj.show_info()


# class Student:
#     name = 'Prakhar'
#     roll = 154
#     age = 19
#     branch = 'CSE'
#     def __init__(self,college,city):
#         #instance variable
#         self.college = college
#         self.city = city
#         print('executed')
    
#     def show_info(self):
#         print(self.name)
#         print(self.college)
#     class Teacher:
#         hello = 'hola'
#         def __init__(self):
#             print('Hello subclass')
# obj1 = Student('IIT Sitapura','Jaipur')
# obj2 = Student('IIT Patna','Patna')
# # print(obj1.name)
# # print(obj1.college)
# # print(obj1.city)
# # print(obj2.name)
# # print(obj2.college)
# # print(obj2.city)
# obj1.show_info()
# obj2.show_info()


class Student:
    name = 'Prakhar'
    roll = 154
    age = 19
    branch = 'CSE'
    def __init__(self,college,city):
        #instance variable
        self.college = college
        self.city = city
        print('Hello Student')
    
    def show_info(self):
        print(self.name)
        print(self.college)

    #class method
    @classmethod
    def show_class_prop(cls):
        print(cls.name)
        print(cls.roll)
    # NESTED CLASS
    class Teacher:
        hello = 'hola'
        def __init__(self): 
            print('Hello Teacher')

# Student_obj = Student('JECRC','JAIPUR')

# Student_obj.show_class_prop()
# Student.show_class_prop()

    @staticmethod
    def Demo_stat():
        print('Hello static method')

obj = Student('IIT SITAPURA', 'Jaipur')
obj.Demo_stat()
Student.Demo_stat()
# Student.show_info() --> Error (instance funtions cannot be called using class name)



