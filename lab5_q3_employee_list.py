employees = []

for i in range(3):
    print(f"\nEmployee {i+1}")
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    salary = float(input("Enter salary: "))

    employee = (name, age, salary)
    employees.append(employee)

print("\nEmployee list:")
print(employees)