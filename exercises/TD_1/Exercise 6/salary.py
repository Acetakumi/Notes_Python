name = input("What is your name: ")
rate = float(input("What is your hourly rate: "))
hours = float(input("How many hours did you work: "))

grossSalary = round(2 * (rate * hours), 2)
contributions = round(grossSalary * 0.14, 2)
net = round(grossSalary - contributions, 2)

print("Biweekly Pay Slip")
print("Employee's Name: " + name)
print("Gross salary: " + str(grossSalary))
print("Social Security Contributions: " + str(contributions))
print("Net Salary: " + str(net))