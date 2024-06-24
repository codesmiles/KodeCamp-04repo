# get the os of the pc
# implement a function that will create a file and there will be restrictions on where the files can be created
import os
from functions import create_group, create_user, assign_user_to_group, creating_file_company_directory

"""_summary_
    1. Using Python, create the following users, and assign them to groups
    Employees:                          groups
    
    Andrew, System Administrator        IT_TEAM
    Julius, Legal                       LEGAL_TEAM
    Chizi, Human Resource Manager       HR_TEAM
    Jeniffer, Sales Manager             SALES_TEAM
    Adeola, Business Strategist         BUSINESS_TEAM
    Bach, CEO                           BUSINESS_TEAM
    Gozie, IT intern                    IT_TEAM
    Ogochukwu, Finance Manager          FINANCE_TEAM
"""

def processing_kodecamp_employees():
    employees_data = {
        # "FOOD_TEAM": [("JOhN", "FOOD SERVICE")],
         "IT_TEAM": [("Andrew", "System Administrator"), ("Gozie", "IT intern")],
         "LEGAL_TEAM": [("Julius", "Legal")],
         "HR_TEAM": [("Chizi", "Human Resource Manager")],
         "SALES_TEAM": [("Jeniffer", "Sales Manager")],
         "BUSINESS_TEAM": [("Adeola", "Business Strategist"), ("Bach", "CEO")],
         "FINANCE_TEAM": [("Ogochukwu", "Finance Manager")],
    }

    for team, employees in employees_data.items():
        group_name = create_group(team)
        if not group_name:
            continue
        print(f"Group '{group_name}' created successfully.")

        for name, role in employees:
            user_data = create_user(name,"")
            if not user_data:
                continue
            print(f"User {user_data} created successfully.")

            assign_user_to_group(user_data, group_name)
            print(
                 f"User {user_data} assigned to group '{group_name}' successfully."
             )

        print(f"user data: {user_data} belongs to group named: {group_name}, ")





"""_summary_
    2. Using Python, create the following directories
    Company Documents (Directories):

    Finance Budgets
    Contract Documents
    Business Projections
    Business Models
    Employee Data
    Company Vision and Mission Statement
    Server Configuration Script

    Include a feature that takes user input and creates a file in your code. User input should include:
    Name of file
    Directory to create the file
    Don't create the file if the Directory name is not one of the company directories.
"""
def task_number_2():    
    file_name = input("Input The name of your file: ")
    directory = input("Input the directory you want to create your file: ")

    creating_file_company_directory(file_name, directory)


def main():
    processing_kodecamp_employees()
    task_number_2()

main()
