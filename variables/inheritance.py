class Student:
    def __init__(self,name,school):
        self.name = name
        self.school = school
        self.marks = []
    def average(self):
        return sum(self.marks)/len(self.marks)

    @classmethod
    def friend(cls,origin,friend_name,*args):
        return cls(friend_name,origin.school, *args)






class WorkingStudent(Student):
    def __init__(self,name,school,salary):
        super().__init__(name,school)
        self.salary = salary


anna = Student("Anna","Oxford")
bob = WorkingStudent("Bob","RIT",20.00)

print(bob.salary)

friend = WorkingStudent.friend(anna,"Greg")

print(friend.name)
print(friend.school)
print(friend.salary)