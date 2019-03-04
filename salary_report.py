# generate a report showing how much each department is spending on employee salaries each quarter.
#
# 1. get depts list
#   2. for each department get employees
#     3. for each employee get their salary history
#       4. for each quarter get salary for that quarter and add to quarter_report list for department
#         - handle salary changes mid quarter
#         - was employee in department whole quarter
#
#   5. print quarter_report list for department after gathering all employee salaries
#      
#!/usr/bin/python
import MySQLdb
from datetime import datetime
from dateutil.relativedelta import *

# date to start fiscal quarters
start_date = '1985-07-01'
end_date = '2002-10-01'

# setup mysql connection string
db = MySQLdb.connect(host="localhost",  # your host 
                     user="root",       # username
                     passwd="password", # password
                     db="employees")    # name of the database

# function: execute mysql queries
def exec_mysql(query):
    cur = db.cursor()
    cur.execute(query)
    return cur.fetchall()

# function: query db for employees in department
def get_dept_employees(dept_id):
    query = "SELECT * FROM dept_emp WHERE dept_no=\'" + dept_id + "\'"
    return exec_mysql(query)

# function: query db for employee salary from employeeID
def get_employee_salary(emp_id, start_date, end_date):
    query = "SELECT * FROM salaries WHERE emp_no=\'" + str(emp_id) + "\' AND to_date BETWEEN \'" + str(start_date) + "\' AND \'" + str(end_date) + "\'"
    return exec_mysql(query)

# function: get all departments in db
def get_departments():
    query = "SELECT * FROM departments"
    return exec_mysql(query)

# function: single quarter report for single department
def print_quarter_report(department_id, department_name, start, three_months_later):
    # start a counter to add up salaries for this quarter and department
    department_quartly_salary_total = 0

    # iterate through list of employees
    for dept_emp in get_dept_employees(department_id):
        # if employee from_date is before or on local start date AND employee to_date is greater or equal than local end date
        #if (dept_emp[2] <= start and dept_emp[3] >= three_months_later):
        if (dept_emp[2] < three_months_later and dept_emp[3] >= three_months_later):
            emp_salary = get_employee_salary(dept_emp[0], start, three_months_later)
            if emp_salary:
                # add to department salary counter for this quarter
                department_quartly_salary_total += int(emp_salary[0][1])

    # print department name, quarter start date and salary total for this quarter
    print department_name, start, department_quartly_salary_total

# function: check if employee was in department during given time period
def department_report(department):
    department_id = department[0]
    department_name = department[1]

    # set local start and end dates from global vars
    start = datetime.strptime(start_date, "%Y-%m-%d").date()
    end = datetime.strptime(end_date, "%Y-%m-%d").date()

    # loop from local start to end date, adding 3 months each iteration for fiscal quarters
    while start <= end:
        # get 3 month later date
        three_months_later = start + relativedelta(months=+3)

        # print each quarter report for this department
        print_quarter_report(department_id, department_name, start, three_months_later)
        
        # last, set start counter equal to 3 months later
        start = three_months_later

# function: execute and display salary report
def run_salary_report():
    # get and loop through departments list
    for department in get_departments():
        # kick off report for this department
        department_report(department)

def main():
    # kick off salary report
    run_salary_report()

if __name__ == "__main__":
   main()
