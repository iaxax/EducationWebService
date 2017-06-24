#coding:utf-8

from spyne import Application, srpc, Iterable, Unicode, Integer
from spyne.service import ServiceBase
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from service.course import CourseService
from service.student import StudentService
from model.statistics import CourseStatisticsInfo, StudentStatisticsInfo
from model.course import CourseInfo

class CourseWebService(ServiceBase):

	# 获得课程统计信息
	@srpc(_returns=Iterable(CourseStatisticsInfo))
	def getCourseStatistics():
		return CourseService.getCourseStatistics()

	# 获得学生统计信息
	@srpc(_returns=Iterable(StudentStatisticsInfo))
	def getStudentStatistics():
		return StudentService.getStudentStatistics()

	# 获取课程信息
	@srpc(_returns=Iterable(CourseInfo))
	def getAllCourseInfo():
		return CourseService.getAllCourseInfo()

	# 根据ID列表获取相应课程信息
	@srpc(Unicode, _returns=Iterable(CourseInfo))
	def getCourseByIds(idStr):
		return CourseService.getCourseInfoByIds(idStr.split(','))


	# # 获取学生的所选课程
	# @srpc(Integer, _returns=Iterable(CourseInfo))
	# def getSelectCourseInfo(studentId):
	# 	return StudentService.getSelectCourseInfo(studentId)

application = Application(
		[CourseWebService], 'edu.nju.software.education.soap',
        in_protocol=Soap11(validator='lxml'),
         out_protocol=Soap11()
)

wsgi_application = WsgiApplication(application)


if __name__ == '__main__':
    import logging

    from wsgiref.simple_server import make_server

    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger('spyne.protocol.xml').setLevel(logging.DEBUG)

    logging.info("listening to http://127.0.0.1:8000")
    logging.info("wsdl is at: http://localhost:8000/?wsdl")

    server = make_server('127.0.0.1', 8000, wsgi_application)
    server.serve_forever()


