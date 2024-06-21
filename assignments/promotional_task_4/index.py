# get the os of the pc
# implement a function that will create a file and there will be restrictions on where the files can be created
import os
from functions import create_group, create_user, assign_user_to_group

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
            user_data = create_user(name, "")
            # if not user_data:
            #     continue
            # print(f"User '{user_data['username']}' created successfully.")

            assign_user_to_group(user_data["username"], group_name)
        #     print(
        #         f"User '{user_data["username"]}' assigned to group '{group_name}' successfully."
        #     )

        # print(f"user data: {user_data} belongs to group named: {group_name}, ")


def creating_file_company_directory(
    name_of_file: str, directory_to_create_the_file: str
):
    root = "company_files" 
    company_dir = [
        "Finance Budgets",
        "Contract Documents",
        "Business Projections",
        "Business Models",
        "Employee Data",
        "Company Vision And Mission Statements",
        "Server Configuration Scripts",
    ]
    
    if len(directory_to_create_the_file) < 1:
        print(
            "The directory should not be empty."
        )
        return False
    
    if str.title(directory_to_create_the_file) not in company_dir:
        print(
            f"The directory {directory_to_create_the_file} does not exist"
        )
        return False
    
    if not os.path.exists(root):
        os.mkdir(f'{root}')
        print(f"directory created in {os.getcwd()}")
        
    os.chdir(f'{root}')
    print(f"directory changed to {os.getcwd()}")
    
    if not os.path.exists(directory_to_create_the_file):
        os.mkdir(directory_to_create_the_file)
        print(f"directory created in {os.getcwd()}")
    
    os.chdir(directory_to_create_the_file)
    print(f"directory changed to {os.getcwd()}")

    if os.path.exists(name_of_file):
        print(
            f"The file {name_of_file} already exists."
        )
        return False
    
    with open(f'{name_of_file}.txt', "w") as file:
        file.write("Hello, World! \n\n delete this text when you see this")

file_name = input("Input The name of your file: ")
directory = input("Input the directory you want to create your file: ")

creating_file_company_directory(file_name, directory)


def main():
    processing_kodecamp_employees()


# main()
