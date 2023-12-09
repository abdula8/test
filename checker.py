import os
import subprocess

def check_and_clone(directory_path, git_repo_url):
    if os.path.exists(directory_path) and os.path.isdir(directory_path):
        print(f"The directory '{directory_path}' exists.")
    else:
        print(f"The directory '{directory_path}' does not exist. Cloning from the repository.")
        subprocess.run(["git", "clone", git_repo_url, directory_path])
    # Change the working directory to the specified one
    # os.chdir(directory_path)
    # print(f"Changed working directory to: {os.getcwd()}")
# Example usage:
directory_to_check = "./odoo"
git_repository_url = "https://github.com/abdula8/odoo.git"

check_and_clone(directory_to_check, git_repository_url)
