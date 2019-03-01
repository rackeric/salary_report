# generate a report showing how much each department is spending on employee salaries each quarter.
#
# 1. get depts list
#   2. for each department get employees
#     3. for each employee get their salary history
#       4. for each quarter get salary for that quarter and add to quarter_report array for department
#         - handle salary changes mid quarter
#         - was employee in department whole quarter
#
#   5. print quarter_report array for department after gathering all employee salaries
#      
#!/usr/bin/python
import MySQLdb
from datetime import datetime
from dateutil.relativedelta import *

# database connection string 
db = MySQLdb.connect(host="localhost",  # your host 
                     user="root",       # username
                     passwd="password",     # password
                     db="employees")   # name of the database

# date to start fiscal quarters
start_date = '1980-10-01'
end_date = '2020-12-31'
 
# Create a Cursor object to execute queries.
cur = db.cursor()
 
# Select data from table using SQL query.
cur.execute("SELECT * FROM departments")
 
# get deparments list
for department in cur.fetchall():
    print department[1]
    dept_employees_cur = db.cursor()
    dept_num = department[0]
    dept_employees_cur.execute("SELECT * FROM dept_emp WHERE dept_no=\'" + dept_num + "\'")
    employees = dept_employees_cur.fetchall()

    start = datetime.strptime(start_date, "%Y-%m-%d")
    end =datetime.strptime(end_date, "%Y-%m-%d")
    while start <= end:
        print "Quarter: ", start
        three_months_later = start + relativedelta(months=+3)

	#if (datetime.strptime(str(dept_emp[2]), "%Y-%m-%d") <= datetime.strptime(start, "%Y-%m-%d") and datetime.strptime(str(dept_emp[3]), "%Y-%m-%d") >= datetime.strptime(end, "%Y-%m-%d")):
	
        # iterate through list of employees
        for dept_emp in employees:
            if (datetime.strptime(str(dept_emp[2]), "%Y-%m-%d") <= start and datetime.strptime(str(dept_emp[3]), "%Y-%m-%d") >= end):
                print dept_emp[0], " ", dept_emp[1], " ", dept_emp[2], " ", dept_emp[3]

        start = three_months_later


def is_between_dates(from_date, to_date):
    # see if between 2 dates
    return true;
