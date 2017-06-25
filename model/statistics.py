#encoding:utf-8

from spyne import Unicode
from spyne.model.complex import ComplexModel
from department import departmentId

class CourseStatisticsInfo(ComplexModel):

    courseid = None
    studentNum = None
    name = None
    institution = unicode(departmentId)
    
    _type_info = {
        'courseid': Unicode,
        'studentNum': Unicode,
        'name': Unicode,
        'institution': Unicode
    }

    def __init__(self, courseId, studentNum, name):
        self.courseId = courseId
        self.studentNum = studentNum
        self.name = name


class StudentStatisticsInfo(ComplexModel):
    studentid = None
    courseNum = None
    name = None
    institution = unicode(departmentId)

    _type_info = {
        'studentid': Unicode,
        'courseNum': Unicode,
        'name': Unicode,
        'institution': Unicode
    }

    def __init__(self, studentId, courseNum, name):
        self.studentid = studentId
        self.courseNum = courseNum
        self.name = name

    