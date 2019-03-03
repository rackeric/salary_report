# salary_report
a report showing how much each department is spending on employee salaries each quarter.

# Requirements
* CentOS library install instructions provided.
* MySQL running on localhost with root password set to 'password', or change in script.
* employees.sql MySQL db (included) from https://github.com/datacharmer/test_db

Install required libraries:
    
    yum install MySQL-python
    yum install python-dateutil

Import employees db in to MySQL database:
    
    mysql < employees.sql

# To Run
    python salary_report.py

# Performance
This takes around 35 minutes to run on a Rackspace Public Cloud server using 1 GB General Purpose v1 flavor (1G RAM/1vcpu)

# To Test
Test check functions for expected SQL queries and report function for expected output.
    pip install pytest unittest mock
    pytest -vvv test_salary_report.py 
