# salary_report
This script is used to generate a report showing how much each department is spending on employee salaries each quarter.

# Requirements
* CentOS library install instructions provided.
* MySQL running on localhost with root password set to 'password', or change in script.
* Follow instructions to import employees.sql MySQL db (included) from https://github.com/datacharmer/test_db

Install required libraries:
    
    yum install -y MySQL-python python-dateutil python2-pip

# To Run
    python salary_report.py

Example output:

    Customer Service 1985-10-01 40000
    Customer Service 1986-01-01 8019391
    Customer Service 1986-04-01 10710073

# Performance
This takes around 45 minutes to run on a Rackspace Public Cloud server using 1 GB General Purpose v1 flavor (1G RAM/1vcpu)

# To Test
Test check functions for expected SQL queries and report function for expected output.

    pip install pytest unittest mock
    pytest -vvv test_salary_report.py 
