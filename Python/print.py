# -*- coding:utf-8 -*-
user="Alex"
age=35
job='IT'
salary=5000
#以下为三种格式化输出方式，第二种和第三种其实是一样，只是换一种表达
info1='''
------info of %s------
Name: %s
Age: %s
Job: %s
Salary: %s
----------------------
'''%(user,user,age,job,salary)

info2='''
------info of {_name}------
Name: {_name}
Age: {_age}
Job: {_job}
Salary: {_salary}
----------------------
'''.format(_name=user,
           _age=age,
           _job=job,
           _salary=salary)

info3='''
------info of {0}------
Name: {0}
Age: {1}
Job: {2}
Salary: {3}
----------------------
'''.format(user,age,job,salary)

print info3

'''
import getpass
a=getpass.getpass("password:")
print a
'''