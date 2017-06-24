#coding:utf-8

import sys
sys.path.append('..')

from dao.selectDAO import SelectDAO
from dao.courseDAO import CourseDAO
from model.statistics import CourseStatisticsInfo
from model.course import CourseInfo

class CourseService:

	# 根据课程ID获得选择该课程的人数
	@staticmethod
	def __getSelectStudentNum(courseId):
		return SelectDAO.getSelectStudentNum(courseId)

	# 获取课程统计信息
	@staticmethod
	def getCourseStatistics():
		allInfo = CourseDAO.getAllCourseInfo()
		for info in allInfo:
			num = CourseService.__getSelectStudentNum(info[0])
			yield CourseStatisticsInfo(unicode(info[0]), unicode(num), unicode(info[1]))

	# 获取所有的课程信息
	@staticmethod
	def getAllCourseInfo():
		infos = CourseDAO.getAllCourseInfo()
		for info in infos:
			yield CourseInfo(
				unicode(info[0]), unicode(info[1]), unicode(info[2]),
				unicode(info[3]), unicode(info[4]), unicode(info[5])
			)

	# 根据ID列表获取相应课程
	@staticmethod
	def getCourseInfoByIds(ids):
		for id in ids:
			infos = CourseDAO.getCourseInfoById(int(id))
			for info in infos:
				yield CourseInfo(
					unicode(info[0]), unicode(info[1]), unicode(info[2]),
					unicode(info[3]), unicode(info[4]), unicode(info[5])
				)

		
	