# -*- coding: utf-8 -*-
# This app generates seating charts for classroom use
#
# Classes
# -------
# Student - an individual person who needs a Seat during a particular period
#           .label, string for name/student number/other identifier
#           .positive, list of Students that increase score
#           .negative, list of Students that decrease score
#           .need, list of strings that indicates a need location
#                   limited to teachers'...: 'front','back','left','right'
#           .proximity, string that indicates how close to the teacher
#                   limited to...: 'near','medium','far'
#
# Seat - an individual location where a Student sits in a Classroom
#           .x, integer from 0 to m indicating left(0)/right(m) position
#           .y, integer from 0 to n indicating front(0)/back(n) position
#
# Classroom - the space in which multiple Seats are arranged
#           .label, string for classroom/period/teacher/other identifier
#           .width, integer m, the maximum number of seats left(0) to right(m)
#           .depth, integer n, the maximum number of seats front(0) to back(n)
#           .roster, list of Students available to be seated
#           .assignments, a paired listing of Seats and Students
#
#
# Operations
# ----------
# Import - import a list of student names and attributes (txt,xls,csv)
# Randomize - shuffle students among seats
# Optimize - score an seating chart based on student constraints (needs/wants)
# Copy - deep copy a seating chart for forking
# Save - save a chart to a file for archiving
# Load - load a chart from a file for use
# Export - export a chart to a useable output (png, xls, csv, txt)


class Student:
    """ Person """
    def __init__(self, label):
        self.label = label
        self.positive = []
        self.negative = []
        self.need = []
        self.proximity = ''

    def __repr__(self):
        s = 'label = ' + self.label + '\n\n'
        s = s + self.positivestring()
        s = s + self.negativestring()
        return s

    def positivestring(self):
        s = 'positive\n'
        s = s + '--------\n'
        if not self.positive:
            s = s + 'None\n'
        else:
            for i in self.positive:
                s = s + i.label + '\n'
        s = s + '\n'
        return s

    def negativestring(self):
        s = 'negative\n'
        s = s + '--------\n'
        if not self.negative:
            s = s + 'None\n'
        else:
            for i in self.negative:
                s = s + i.label + '\n'
        s = s + '\n'
        return s

    def addstudent(self, stud, sign):
        """ Adds a Student object to the list of positives '+' or negatives '-'
        """
        if sign == '+':
            self.positive.append(stud)
            s = self.positivestring()
        elif sign == '-':
            self.negative.append(stud)
            s = self.negativestring()
        return s

    def removestudent(self, stud, sign):
        """ Removes a Student object from positives '+' or negatives '-'
        """
        if sign == '+':
            try:
                self.positive.remove(stud)
            except ValueError:
                print('Student ' + stud.label +
                      ' isn\'t in the list of positives')
                return None
            s = self.positivestring()
        elif sign == '-':
            try:
                self.negative.remove(stud)
            except ValueError:
                print('Student ' + stud.label +
                      ' isn\'t in the list of negatives')
                return None
            s = self.negativestring()
        return s


class Seat:
    """ Location """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return str(self.x) + ', ' + str(self.y)


class Classroom:
    """ Space """
    def __init__(self, label, width, depth):
        self.label = label
        self.width = width
        self.depth = depth
        self.roster = []
        self.assignments = []
        
    def __repr__(self):
        s = 'label = ' + self.label + '\n\n'
        s = s + 'width: ' +  str(self.width) + '\n'
        s = s + 'depth: ' +  str(self.depth) + '\n'
        s = s + '\nRoster\n'
        s = s + '------\n'
        s = s + ''.join(self.roster)
        s = s + '\nAssignments\n'
        s = s + '-----------\n'
        s = s + ''.join(self.assignments)
        return s


class_room = Classroom('1st Period Advanced',5,5)
print(class_room)


#seat_1 = Seat(0, 0)
#print(seat_1)


#st_1 = Student('One')
#st_2 = Student('Two')
#st_3 = Student('Three')
#
#print(st_1)
#print(st_2)
#print(st_3)
#
#print(st_1.addstudent(st_2, '+'))
#print(st_1.removestudent(st_2, '+'))
#print(st_1.removestudent(st_2, '+'))
#
#print(st_1.addstudent(st_3, '-'))
#print(st_1.removestudent(st_3, '-'))
#print(st_1.removestudent(st_3, '-'))
