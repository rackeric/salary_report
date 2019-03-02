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
start_date = '1985-10-01'
end_date = '2002-10-01'

# function: query db for employees in department
def get_dept_employees(department):
    dept_employees_cur = db.cursor()
    dept_num = department[0]
    dept_employees_cur.execute("SELECT * FROM dept_emp WHERE dept_no=\'" + dept_num + "\'")
    return dept_employees_cur.fetchall()

# function: query db for employee salary from employeeID
def get_employee_salary(emp_id, start_date, end_date):
    # TODO: what if find multiple salaries for that time
    employee_salary_cur = db.cursor()
    employee_salary_cur.execute("SELECT * FROM salaries WHERE emp_no=\'" + str(emp_id) + "\' AND to_date BETWEEN \'" + str(start_date) + "\' AND \'" + str(end_date) + "\'")
    return employee_salary_cur.fetchall()

# function: salary report
def run_salary_report():
    # Create a Cursor object to execute queries.
    depts_cur = db.cursor()
     
    # Select data from table using SQL query.
    depts_cur.execute("SELECT * FROM departments")

    # get and loop through departments list
    for department in depts_cur.fetchall():

        # get employees for this department
        employees = get_dept_employees(department)

        # set local start and end dates so to preserve master start_date and end_date for use on next for loop iteration
        start = datetime.strptime(start_date, "%Y-%m-%d").date()
        end = datetime.strptime(end_date, "%Y-%m-%d").date()

        # loop from local start to end dates, adding 3 months each iteration for fiscal quarters
        while start <= end:

            # get 3 month later date
            three_months_later = start + relativedelta(months=+3)

            # start a counter to add up salaries for this quarter and department
            department_quartly_salary_total = 0
            
            # iterate through list of employees
            for dept_emp in employees:
                # if employee from_date is before or on local start date AND employee to_date is greater or equal than local end date
                if (dept_emp[2] <= start and dept_emp[3] >= end):
                    emp_salary = get_employee_salary(dept_emp[0], start, three_months_later)
                    if emp_salary:
                        # add to department salary counter for this quarter
                        department_quartly_salary_total += int(emp_salary[0][1])

            # print department name, quarter start date and salary total for this quarter
            print department[1], start, department_quartly_salary_total
            
            # last, set start counter equal to 3 months later
            start = three_months_later

            # end of while loop

    # end of for loop

# kick off salary report
run_salary_report()

# end of script
