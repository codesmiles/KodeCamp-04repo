# Promotional Task Workflow😁

## Table of Contents

- [Promotional Task Workflow😁](#promotional-task-workflow)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Precaution](#precaution)
  - [Promotional task 4 Instructions](#promotional-task-4-instructions)
  - [Solution](#solution)
    - [**CLICK HERE TO SEE THE FUNCTIONS**](#click-here-to-see-the-functions)
    - [**CLICK HERE TO SEE WHERE THE FUNCTIONS ARE BEING IMPORTED AND EXECUTED**](#click-here-to-see-where-the-functions-are-being-imported-and-executed)
  - [Conclusion](#conclusion)


## Introduction

In the process of working on this project I made mistakes which lead to the loss of many important Recources.
Here are the task done on this project.

## Precaution

- Make sure you're running any script in a virtual environment like in vagrant or docker🥴.
- Should you plan recreate this project in the future remember to learn about virtual environment and understand the shell commands so you can explain where an issue comes from should the case arise.

## Promotional task 4 Instructions

Attempt all questions. Upload code to Github and share the repository link
Use Functional Programming principles to make your code readable (DRY, KISS)
Do your research and find modules to help you accomplish your task. You can also create your own modules.

![](assets/unnamed.png)

As a DevOps Engineer, you have been consulted to set up the infrastructure servers of a small business. Automate the creation of the following users and directories using Python.

1. Using Python, create the following users, and assign them to groups
Employees:

Andrew, System Administrator
Julius, Legal
Chizi, Human Resource Manager
Jeniffer, Sales Manager
Adeola, Business Strategist
Bach, CEO
Gozie, IT intern
Ogochukwu, Finance Manager

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

## Solution

### [**CLICK HERE TO SEE THE FUNCTIONS**](functions.py)

### [**CLICK HERE TO SEE WHERE THE FUNCTIONS ARE BEING IMPORTED AND EXECUTED**](index.py)

- First task
  - set up vagrant virtual machine
    ![vagrant int](assets/vagrant_init.png)

  - install ubuntu os on the machine and access your shell
    ![vagrant server](assets/run_ubuntu_server.png)
    ![vagrant ssh](assets/vagrant_ssh.png)

  - install python language on the machine
    ![update ubuntu](assets/update_ubuntu.png)
    ![install python](assets/install_python.png)
  - make a directory for the project
    ![mkdir](assets/mkdir.png)
  - write a function to create user, create group and assign user to a group.
    ![result](assets/result.png)
    ![result](assets/result-2.png)
- second task
  - write a function to make directory on the projects
  - added conditions to prevent any directory that's not listed to be created
  
```py
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
  ```
  
## Conclusion

The workings of this task is located within the the directory of this project. Do well to check them out.

Good Luck Comrade🫡