def gross_salary(basic_salary, allowance):
    return basic_salary + allowance


def epf(gross_salary):
    return gross_salary * 0.11


def socso(gross_salary):
    return gross_salary * 0.005


def net_salary(gross_salary, epf_amount, socso_amount):
    return gross_salary - epf_amount - socso_amount
