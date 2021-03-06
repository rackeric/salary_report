# salary_report
This script is used to generate a report showing how much each department is spending on employee salaries each quarter.

# Requirements
* Required libraries install instructions provided for CentOS 7 with `epel-release` repo installed.
* MySQL running on localhost with root password set to 'password', or change db connection string in script.
* Follow instructions at https://github.com/datacharmer/test_db to import `employees.sql` MySQL db.

Install required libraries:
    
    yum install -y MySQL-python python-dateutil python2-pip

# To Run
    python salary_report.py

Output:

    [Department Name] [Quarter Start Date] [Total Spent on Salaries for that Quarter]

Example output:

    Customer Service 1985-10-01 40000
    Customer Service 1986-01-01 8019391
    Customer Service 1986-04-01 10710073

# Performance
This takes around 46 minutes to run on a Rackspace Public Cloud server using 1 GB General Purpose v1 flavor (1G RAM/1vcpu)

# To Test
Tests check functions for expected SQL queries and report function for expected output. Upgrade pip and install needed pip modules for testing.

    pip install --upgrade pip
    pip install pytest mock
    pytest -vvv test_salary_report.py 

Example:

    # pytest -vv test_salary_report.py 
    ===================================== test session starts =====================================
    platform linux2 -- Python 2.7.5, pytest-4.3.0, py-1.8.0, pluggy-0.9.0 -- /usr/bin/python2
    cachedir: .pytest_cache
    rootdir: /root/salary_report, inifile:
    collected 6 items                                                                             
    
    test_salary_report.py::test_get_dept_employees PASSED                                   [ 16%]
    test_salary_report.py::test_get_employee_salary PASSED                                  [ 33%]
    test_salary_report.py::test_get_departments PASSED                                      [ 50%]
    test_salary_report.py::test_department_report PASSED                                    [ 66%]
    test_salary_report.py::test_print_quarter_report PASSED                                 [ 83%]
    test_salary_report.py::test_run_salary_report PASSED                                    [100%]
    
    ================================== 6 passed in 0.07 seconds ===================================
