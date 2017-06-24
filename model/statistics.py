#encoding:utf-8

from spyne import Unicode
from spyne.model.complex import ComplexModel
from department import departmentId

class CourseStatisticsInfo(ComplexModel):

    courseId = None
    studentNum = None
    name = None
    institutionId = unicode(departmentId)
    
    _type_info = {
        'courseId': Unicode,
        'studentNum': Unicode,
        'name': Unicode,
        'institutionId': Unicode
    }

    def __init__(self, courseId, studentNum, name):
        self.courseId = courseId
        self.studentNum = studentNum
        self.name = name


class StudentStatisticsInfo(ComplexModel):
    studentId = None
    courseNum = None
    name = None
    institutionId = unicode(departmentId)

    _type_info = {
        'studentId': Unicode,
        'courseNum': Unicode,
        'name': Unicode,
        'institutionId': Unicode
    }

    def __init__(self, studentId, courseNum, name):
        self.studentId = studentId
        self.courseNum = courseNum
        self.name = name

    