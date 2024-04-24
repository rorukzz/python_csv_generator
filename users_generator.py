import csv
import random
from faker import Faker

# Generate a list of column names
column_names = ["User_ID", "First_Name", "Last_Name", "Email", "Phone_Number", "Gender", "Date_of_Birth", "Department", "Position", "Manager_ID", "Join_Date", "Salary", "Address", "City", "State", "Country", "Postal_Code"]

# Generate some mock data using Faker
fake = Faker()

# Generate a list of users
users = []
for i in range(1, 10000):  # Generate data for 100 users
    user = {
        "User_ID": i,
        "First_Name": fake.first_name(),
        "Last_Name": fake.last_name(),
        "Email": fake.email(),
        "Phone_Number": fake.phone_number(),
        "Gender": random.choice(["Male", "Female"]),
        "Date_of_Birth": fake.date_of_birth(minimum_age=18, maximum_age=90),
        "Department": fake.random_element(elements=("HR", "Finance", "IT", "Marketing", "Sales")),
        "Position": fake.random_element(elements=("Manager", "Supervisor", "Associate", "Intern")),
        "Manager_ID": random.randint(1, 10),
        "Join_Date": fake.date_this_decade(),
        "Salary": round(random.uniform(30000, 100000), 2),
        "Address": fake.street_address(),
        "City": fake.city(),
        "State": fake.state_abbr(),
        "Country": fake.country(),
        "Postal_Code": fake.postcode(),
    }
    users.append(user)

# Write data to a CSV file
with open("users.csv", "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=column_names)
    writer.writeheader()
    for user in users:
        writer.writerow(user)

print("CSV file 'users.csv' has been generated successfully.")
