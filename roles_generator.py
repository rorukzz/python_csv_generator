import csv
import random


# Generate a list of column names for the roles CSV
roles_column_names = ["Role_ID", "Position", "Responsibilities"]

# Generate some mock data using Faker for roles
roles = [
    {"Role_ID": 1, "Position": "Manager", "Responsibilities": "Oversee and coordinate the daily operations of the department."},
    {"Role_ID": 2, "Position": "Supervisor", "Responsibilities": "Supervise the work of employees in the department and ensure the team meets its goals."},
    {"Role_ID": 3, "Position": "Associate", "Responsibilities": "Carry out tasks assigned by the manager or supervisor and contribute to the team's success."},
    {"Role_ID": 4, "Position": "Intern", "Responsibilities": "Assist with day-to-day tasks, learn from colleagues, and contribute to projects as assigned."},
]

# Write role data to a CSV file
with open("roles.csv", "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=roles_column_names)
    writer.writeheader()
    for role in roles:
        writer.writerow(role)

print("Roles CSV Generated Successfully")
