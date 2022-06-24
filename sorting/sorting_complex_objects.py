from operator import attrgetter, itemgetter

class Employee:
    
    def __init__(self, name, staff_no, salary):
        self.name = name
        self.staff_no = staff_no
        self.salary = salary
    
    def __repr__(self):
        return repr((self.name, self.staff_no, self.salary))



if __name__ == '__main__':
    employees = [
        Employee('Dave', 173, 122000),
        Employee('Dyke', 172, 122000),
        Employee('Jake', 124, 142000),
        Employee('John', 143, 95000),
        Employee('Jane', 193, 100000),
    ]
    # sorting by age alone in a ascending order
    sorted_employees = sorted(employees, key=lambda employee:employee.salary)
    # sorting by salary in a descending order
    sort_by_salary_desc = sorted(employees, key=lambda employee:employee.salary, reverse=True)
    # sorting by two attrs(salary & staff_no) by salary fast then staff_no
    multiple_level_sorting = sorted(employees, key=attrgetter('salary', 'staff_no'))
    # multiple_level_sorting_2 = sorted(employees, key=itemgetter(1,2))
    # NB: Sorts are guaranteed to be stable. That means that when multiple records have 
    # the same key, their original order is preserved.
    print(f"Ascending order: {sorted_employees}")
    print(f"Descending order: {sort_by_salary_desc}")
    print(f"Multiple level sorting: { multiple_level_sorting}")
    # print(f"Multiple level sorting 1: { multiple_level_sorting_2}")