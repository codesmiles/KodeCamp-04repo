import os
import sys
import platform
import subprocess


# create groups
def create_group(group_name: str):
    os_type = platform.system()
    try:
        if os_type == "Darwin":
            # macOS command to create a group
            subprocess.run(["sudo", "dscl", ".", "-create", f"/Groups/{group_name}"], check=True)
            print(f"Group '{group_name}' created successfully on macOS.")
        else:
            print(f"Unsupported OS: {os_type}")
            return False
        
        return group_name
    except subprocess.CalledProcessError as e:
        print(f"create_group Error: {e}")
        return False


# create user
def create_user(username: str, password: str):
    os_type = platform.system()
    try:
        if os_type == "Darwin":
            # macOS command to create a user using sysadminctl
            subprocess.run(["sudo", "sysadminctl", "-addUser", username, "-password", password], check=True)
            print(f"User '{username}' created successfully on macOS.")
        else:
            print(f"Unsupported OS: {os_type}")
            return False
        return {
            "username": username,
            "pwd": password,
        }
    except subprocess.CalledProcessError as e:
        print(f"Error creating user '{username}': {e}")
        return False


# assign user to groups
def assign_user_to_group(username: str, group_name: str):
    try:
        if platform.system() == "Windows":
            subprocess.run(
                ["net", "localgroup", group_name, username, "/add"], check=True
            )

        subprocess.run(["sudo", "adduser", username, group_name], check=True)
       
    except subprocess.CalledProcessError as e:
        print(f"Error assigning user '{username}' to group '{group_name}': {e}")
        return False


# user create file and directories
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
    return True