class Employee:
    
    def __init__(self, name, staff_no, salary):
        self.name = name
        self.staff_no = staff_no
        self.salary = salary
    
    def __repr__(self):
        return repr((self.name, self.staff_no, self.salary))



if __name__ == '__main__':
    employees = [
        Employee('Dave', 123, 122000),
        Employee('Jake', 124, 142000),
        Employee('John', 143, 95000),
        Employee('Jane', 193, 100000),
    ]
    sorted_employees = sorted(employees, key=lambda employee:employee.salary)
    sort_by_salary_desc = sorted(employees, key=lambda employee:employee.salary, reverse=True)
    print(f"Ascending order: {sorted_employees}")
    print(f"Descending order: {sort_by_salary_desc}")
    