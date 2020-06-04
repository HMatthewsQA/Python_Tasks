class Student:
    name = 'student'
    age = 'student'
    class_ = 'student'

    def __init__(self, name, age, class_):
        self.name = name
        self.age = age
        self.class_ = class_

    def avg_test(self, test1, test2, test3):
        self.test1 = test1
        self.test2 = test2
        self.test3 = test3
        avg = (test1 + test2 + test3)/3
        print(avg)
        return avg

#John = Student("John", "21","A")
#print(getattr(John, "age"))
#John.avg_test(3,5,7)

