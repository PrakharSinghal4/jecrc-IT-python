# inheritance

# Single inheritance
# Multiple inheritance
# Multi-level inheritance
# Hierarchial inheritance
# Hybrid inheritance



class Parent:
    name = 'Prakhar Singhal'
    age = 19
    income = '55 LPA'
    def __init__(self,father_name,mother_name):
        self.father_name = father_name
        self.mother_name = mother_name

    def work(self):
        print(self.father_name)
        print(self.mother_name)
        print(self.child_name)
        print(self.child_job)

class Parent2:
    name = 'Rahul Tiwari'
    age = 19
    income = '18 LPA'
    def __init__(self,father_name,mother_name):
        self.father_name = father_name
        self.mother_name = mother_name

    def work(self):
        print(self.father_name)
        print(self.mother_name)



class Child(Parent):
    name = 'Ritik Jain'
    age = 10
    kaam = 'berozgar'
    def __init__(self,child_name,child_job,father_name,mother_name,parent_name2,parent_job2):
        self.child_name = child_name
        self.child_job = child_job
        super().__init__(father_name=father_name,mother_name=mother_name)

    def child_info(self):
        print(self.child_name)
        print(self.child_job)

child_obj = Child('Ritik','lofer', 'Rahul','Matashree')
child_obj.work()






# child_obj = Child()
# # child_obj.child_info()
# child_obj.work()
# # print(child_obj.income)
