"""
    problem z domyslnymi argumentami bedacymi mutowalnymi zmiennymi (lista, slownik, set)
"""

employees = ['Ala', 'Ola', 'Ula']


def add_employee(employee, employees=[]):
    print(employees)
    employees.append(employee)
    print(employees)


add_employee("Roman")
add_employee("Kupidyn")