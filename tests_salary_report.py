import mock
from salary_report import get_dept_employees, get_employee_salary, run_salary_report, get_departments, department_report, print_quarter_report, run_salary_report

@mock.patch('salary_report.exec_mysql')
def test_get_dept_employees(mysql_mock):
    get_dept_employees('12345')
    mysql_mock.assert_called_with("SELECT * FROM dept_emp WHERE dept_no='12345'")

@mock.patch('salary_report.exec_mysql')
def test_get_employee_salary(mysql_mock):
    get_employee_salary('12345', '1988-02-02', '1992-12-12')
    mysql_mock.assert_called_with("SELECT * FROM salaries WHERE emp_no='12345' AND to_date BETWEEN '1988-02-02' AND '1992-12-12'")

@mock.patch('salary_report.exec_mysql')
def test_get_departments(mysql_mock):
    get_departments()
    mysql_mock.assert_called_with("SELECT * FROM departments")

@mock.patch('salary_report.exec_mysql')
def test_department_report(mysql_mock, capsys):
    department_report(['12345', "Test Department"])
    mysql_mock.assert_called_with("SELECT * FROM dept_emp WHERE dept_no='12345'")
    #captured = capsys.readouterr()

@mock.patch('salary_report.exec_mysql')
def test_print_quarter_report(mysql_mock, capsys):
    print_quarter_report('12345', "Test Department", "1985-10-01", "1985-12-31")
    mysql_mock.assert_called_with("SELECT * FROM dept_emp WHERE dept_no='12345'")
    captured = capsys.readouterr()
    assert captured.out == "Test Department 1985-10-01 0\n"

@mock.patch('salary_report.exec_mysql')
def test_run_salary_report(mysql_mock):
    run_salary_report()
    mysql_mock.assert_called_with("SELECT * FROM departments")

test_get_dept_employees()
test_get_employee_salary()
test_get_departments()
test_run_salary_report()
