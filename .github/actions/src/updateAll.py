import os
import glob
import subprocess

def read_config_from_env():
    # Read configuration from environment variables or use default values
    url = os.environ.get('INPUT_LB_DEVOPS_URL')
    driver = os.environ['INPUT_LB_DEVOPS_DRIVER']
    username = os.environ['INPUT_LB_DEVOPS_USER']
    password = os.environ['INPUT_LB_DEVOPS_PASSWORD']
    return url,driver, username, password

def run_liquibase_update(changelog_file, url, driver, username, password):
    # Construct the Liquibase update command
    command = [
        "docker", "run", "--rm",
        "-v", f"{os.getcwd()}:/liquibase",
        "liquibase/liquibase",
        "--changeLogFile", changelog_file,
        "--url", url,
        "--driver", driver,
        "--username", username,
        "--password", password,
        "update"
    ]

    # Run the Liquibase update command
    result = subprocess.run(command, capture_output=True, text=True)

    # Print the Liquibase output
    print(result.stdout)
    print(result.stderr)

def main():
    # Define the path to the migrations folder (assuming it's in the root of the repository)
    migrations_folder = "migrations"

    # Use glob to find all XML files in the migrations folder
    changelog_files = glob.glob(os.path.join(migrations_folder, "*.xml"))
    # Set your database connection details
    url, driver, username, password = read_config_from_env()

    # Iterate through the changelog files and run Liquibase update for each
    for changelog_file in changelog_files:
        run_liquibase_update(changelog_file, url, driver, username, password)

if __name__ == "__main__":
    main()
