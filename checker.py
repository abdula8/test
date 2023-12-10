import os
import subprocess
import sys
"""
This script is used to automate the deployment process of odoo project on AWS sever
"""
def check_and_clone(directory_path, git_repo_url):
    if os.path.exists(directory_path) and os.path.isdir(directory_path):
        print(f"The directory '{directory_path}' exists.")
    else:
        print(f"The directory '{directory_path}' does not exist. Cloning from the repository.")
        subprocess.run(["git", "clone", git_repo_url, directory_path])
        
def is_command_running(command):
    ps_command = subprocess.Popen(["ps", "aux"], stdout=subprocess.PIPE)
    output, _ = ps_command.communicate()
    return command.encode() in output

def restart_command(command):
    subprocess.run(["pkill", "-f", command], shell=False)
    subprocess.run(command, shell=True)
    print("Command restarted.")

def start_command(command):
    subprocess.run(command, shell=True)
    print("Command started correctly!!!")
    
if __name__ == "__main__":
    # command_to_run = "python3 odoo-bin --addons-path=addons -d elfate7"
    command_to_run = "python3 odoo-bin --addons-path=addons -r faten -w 123456789 --db_host 10.0.148.116 --database postgres -i base"
    if len(sys.argv) == 2 and sys.argv[1] == "--restart":
        restart_command(command_to_run)
    elif is_command_running(command_to_run):
        print("The command is already running.")
    elif len(sys.argv) == 2 and sys.argv[1] == "https://github.com/abdula8/odoo.git":
        # Example usage:
        directory_to_check = "./odoo"
        # git_repository_url = "https://github.com/abdula8/odoo.git"
        git_repository_url = sys.argv[1]
        check_and_clone(directory_to_check, git_repository_url)
    else:
        restart_command(command_to_run)
