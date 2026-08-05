def print_report(employee_name, employee_id, gross_salary, epf_amount, socso_amount, net_salary):

    print("\n========== SALARY REPORT ==========")
    print(f"Employee Name : {employee_name}")
    print(f"Employee ID   : {employee_id}")
    print("-----------------------------------")
    print(f"Gross Salary  : RM {gross_salary:.2f}")
    print(f"EPF (11%)     : RM {epf_amount:.2f}")
    print(f"SOCSO (0.5%)  : RM {socso_amount:.2f}")
    print("-----------------------------------")
    print(f"Net Salary    : RM {net_salary:.2f}")
    print("===================================")
