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



# # Example usage
# create_group('devs')
# create_user('alice', 'password123')
# assign_user_to_group('alice', 'devs')
