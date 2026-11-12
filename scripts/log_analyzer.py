#.....................................................................................................................
#.....................................................................................................................
# MY BAD CODE:     
# while True:
#     def analyze_log(file_path,  target_word):
#         try:
#             with open(file_path, 'r') as file_function:

#                 line_count = 0

#                 for file in file_function:
#                     line_count = target_word + 1
#                     print(f"[SUCCESS]:In file {file}, target word {target_word} was found {line_count} times")
                    
                
#             print('[SUCCESS]: Code block ran successfully')

#         except FileNotFoundError:
#             print("File not found. please retry")


# CORRECT CODE:

#Defining the function first.

def analyze_log(file_path, target_word):
    try:
        with open(file_path, 'r') as file_function:
            line_count = 0

            for line in file_function:
                if target_word in line:
                    line_count += 1


            return line_count


    except FileNotFoundError:
        print(f'[ERROR]: File {file_path} has not been found.')
        return None
    

while True:
    user_file = input('Insert your file here please, e.g(logs/raw_firewall.log): ')

    result = analyze_log(user_file, 'BLOCKED')

    if result is not None:
        print(f'[SUCCESS]: Found {result} BLOCKED events in {user_file}')
        break