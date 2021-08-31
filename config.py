# -*- coding: UTF-8 -*-
import hashlib

captcha_url = "http://zhjw.scu.edu.cn/img/captcha.jpg"  # 验证码地址
index_url = "http://zhjw.scu.edu.cn/"  # 主页地址
login_url = "http://zhjw.scu.edu.cn/j_spring_security_check"  # 登录接口
courseSelect_url = "http://zhjw.scu.edu.cn/student/courseSelect/courseSelect/index"  # tokenValue界面
select_url = "http://zhjw.scu.edu.cn/student/courseSelect/selectCourse/checkInputCodeAndSubmit"  # 选课接口
courseList_url = "http://zhjw.scu.edu.cn/student/courseSelect/freeCourse/courseList"  # 选课剩余查询地址
already_select_course_url = "http://zhjw.scu.edu.cn/student/courseSelect/thisSemesterCurriculum/callback"  # 已选课程查询地址
queryTeacherJL_url = "http://zhjw.scu.edu.cn/student/courseSelect/queryTeacherJL"
selectcourse_xueqi = "2021-2022-1-1"
header = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'DNT': '1',
    'Host': 'zhjw.scu.edu.cn',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3782.0 Safari/537.36 Edg/76.0.152.0'
}

with open("config.txt", "r", encoding='utf-8') as f:
    info = f.readlines()
j_username = info[0].strip('\n')
j_password = hashlib.md5(info[1].strip('\n').encode()).hexdigest()
courseNames = info[2].strip('\n').split(';')
# 课程号
courseNums = info[3].strip('\n').split(';')
# 课序号
coursekxhNums = info[4].strip('\n').split(';')
