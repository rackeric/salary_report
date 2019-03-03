# salary_report
a report showing how much each department is spending on employee salaries each quarter.

# Requirements
CentOS install instructions provided.
MySQL running on localhost with root password set to 'password', or change in script.

Install required libraries:
yum install MySQL-python
yum install python-dateutil

Import employees db in to MySQL database:
mysql < employees.sql

# To Run
python salary_report.py

# To Test
pip install pytest unittest mock
pytest -vvv tests_salary_report.py 
