# Name: Ji Yong Hwang

# email: jyhwang@myseneca.ca

class Student:
    def __init__(self, name, number, program):
        programs = ['CNS', 'CTY']
        self.name = name
        self.number = number
        self.courses = {}
        if program in programs:
            self.program = program
        else:
            self.program = 'unknown'

    def __repr__(self):
        return "s.s" % (self.name, self.number)

    def displayStudent(self):
        result = 'Student: '
        result += self.name
        result += '\n'
        result += 'Student ID: '
        result += self.number
        return result

    def get_courses(self):
        newlist = [] 
        newlist.append(str(self.displayStudent()))
        for course in self.courses:
            newlist.append(str(course) + ": " + str(self.courses[course]))
        return newlist

    def __add__(self, t1, gpa=0.0):
        self.courses[t1] = gpa
        return self.courses