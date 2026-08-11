# 🎯 Challenge: scripts/log_checker.py
# Create a new file called scripts/log_checker.py that accomplishes the following:

# Prompt the user to enter a file path to inspect (e.g., logs/blocked_threats.log).

# Wrap the file-opening logic inside a while loop using try / except to catch FileNotFoundError.

# If the file path is invalid, display a custom warning message and loop back to ask for the path again.

# Once a valid file is successfully opened:

# Loop through the file line-by-line to count the total number of lines.

# Print the result: [SUCCESS] Total lines in '<filename>': X

# Break out of the loop and terminate cleanly.

while True:
    file_name = input('Enter suggested file path to access (e.g: logs/blocked_threats.log): ')

    try:
        with open(file_name, 'r') as file:
            line_count = 0
            
            for line in file:
                line_count += 1

                print('\n [ACCESSING CONTENT] \n')
                print(f'\n[SUCCESS]: Total lines in \'{file_name}\': {line_count}')

            break

    except FileNotFoundError:
        print(f'\n File {file_name} not found.')
        print('Please, re-check for correct file name. Effective immediately.')

print('\n[INFO]: Code block exercise ran successfully!')
