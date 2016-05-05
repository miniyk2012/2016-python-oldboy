# -*- coding:utf-8 -*-

class SchoolMember(object):

    member_number = 0

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        self.enroll()

    def enroll(self):
        SchoolMember.member_number += 1
        print('The \033[31;1m[%s] \033[0mSchoolMember [%s] is enrolled!' % (SchoolMember.member_number, self.name))

    def tell(self):
        print("Hello my name is %s" % self.name)

class Teacher(SchoolMember):

    def __init__(self, name, age, sex, course, salary):
        super(Teacher, self).__init__(name, age, sex)  # SchoolMember.__init__(self, name, age, sex)旧式类的写法
        self.course = course
        self.salary = salary

    def teaching(self):
        print('Teacher [%s] is teaching [%s]' %(self.name, self.course))


class Student(SchoolMember):

    def __init__(self, name, age, sex, course, tuition):
        super(Student, self).__init__(name, age, sex)
        self.course = course
        self.tuition = tuition

    def pay_tuition(self):
        print('cao, student [%s] paying tuition [%s]' % (self.name, self.tuition))

t1 = Teacher('alex', 22, 'F', 'PY', 1000)
t2 = Teacher('Tenglan', 25, 'N/A', 'PY', 500)

s1 = Student('SanJiang', 24, 'F', 'python', 15000)
s2 = Student('BaoAn', 24, 'F', 'python', 5000)

t1.tell()
s2.tell()

s1.pay_tuition()
t2.teaching()
