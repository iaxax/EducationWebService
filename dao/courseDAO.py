#encoding=utf-8

from connection.conn import Connection

class CourseDAO:

	# 根据课程ID获取课程信息
	@staticmethod
	def getCourseInfoById(id):
		conn = Connection.getConnection()
		cursor = conn.cursor()
		sql = "select * from course where course_id = %d"%(id)
		cursor.execute(sql)
		return cursor.fetchall()

	# 获取课程信息
	@staticmethod
	def getAllCourseInfo():
		conn = Connection.getConnection()
		cursor = conn.cursor()
		sql = "select * from course"
		cursor.execute(sql)
		return cursor.fetchall()
	
	# 获取选课信息
	@staticmethod
	def getCourseInfo(student_id):
		conn = Connection.getConnection()
		cursor = conn.cursor()
		sql = "select * from course where course_id in \
			(select course_id from selection where student_id = %d)"%(student_id)
		cursor.execute(sql)
		return cursor.fetchall()
	
	# 选课
	@staticmethod
	def selectCourse(student_id, course_id):
		conn = Connection.getConnection()
		cursor = conn.cursor()
		sql = "select * from selection \
			where student_id=%d and course_id=%d"%(student_id, course_id)
		cursor.execute(sql)
		
		if (len(cursor.fetchall()) == 0):
			sql = "insert into selection values(%d, %d)"%(student_id, course_id)
			cursor.execute(sql)
			conn.commit()
			return ('1', u"成功选择该课程")
		else:
			return ('0', u"已经选过该课程")
	
	# 退课
	@staticmethod
	def quitCourse(student_id, course_id):
		conn = Connection.getConnection()
		cursor = conn.cursor()
		sql = "select * from selection \
			where student_id=%d and course_id=%d"%(student_id, course_id)
		cursor.execute(sql)
		
		if (len(cursor.fetchall()) > 0):
			sql = "delete from selection \
				where student_id=%d and course_id=%d"%(student_id, course_id)
			cursor.execute(sql)
			conn.commit()
			return ('1', u"成功退选该课程")
		else:
			return ('0', u"没有选择该课程")

