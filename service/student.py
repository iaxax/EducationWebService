#coding:utf-8

import sys
sys.path.append('..')

from dao.studentDAO import StudentDAO
from dao.selectDAO import SelectDAO
from model.statistics import StudentStatisticsInfo
from model.course import CourseInfo

class StudentService:

	# 根据学生ID获得该学生的选课数目
	@staticmethod
	def __getSelectCourseNum(studentId):
		return SelectDAO.getSelectCourseNum(studentId)

	# 获取学生统计信息
	@staticmethod
	def getStudentStatistics():
		allInfo = StudentDAO.getAllStudentInfo()
		for info in allInfo:
			num = StudentService.__getSelectCourseNum(info[0])
			yield StudentStatisticsInfo(unicode(info[0]), unicode(num), unicode(info[1]))

	# 获取学生所选课程
	@staticmethod
	def getSelectCourseInfo(studentId):
		infos = SelectDAO.getSelectCourseInfo(studentId)
		for info in infos:
			yield CourseInfo(
				unicode(info[0]), unicode(info[1]), unicode(info[2]),
				unicode(info[3]), unicode(info[4]), unicode(info[5])
			)

