#encoding:utf-8

from spyne import Unicode
from spyne.model.complex import ComplexModel
from department import departmentId

class CourseInfo(ComplexModel):
    department_id = unicode(departmentId)
    course_id = None
    name = None
    classroom = None
    classtime = None
    classtype = None
    department = None

    _type_info = {
        'department_id': Unicode,
        'course_id': Unicode,
        'name': Unicode,
        'classroom': Unicode,
        'classtime': Unicode,
        'classtype': Unicode,
        'department': Unicode
    }

    def __init__(self, cid, name, classroom, classtime, classtype, dept):
        self.course_id = cid
        self.name = name
        self.classroom = classroom
        self.classtime = classtime
        self.classtype = classtype
        self.department = dept
