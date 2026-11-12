#ERROR HANDLING!!
# if python doesn't recognize a particular file or code that the user has promted,
# it throws a bunch of readlines and doesn't handle the error very well

# with open('logs/doesnt_exit.txt', 'r') as f:
#     print(f.read())     

#Using the try and except method, it handles code more effienctly

# try:
#     with open('logs/doesnt_exit.txt', 'r') as f:
#         print(f.read())    
# except FileNotFoundError:
#     print('[SYSTEM ALERT] File missing! Check path or permissions.')

while True:
    filename = input('Enter the log file to open(e.g logs/raw_firewall.log): ')

    try:
        with open(filename, 'r') as good_file:
            print("\n=== LOG CONTENTS ===")
            print(good_file.read())
            break

    except FileNotFoundError:
        print(f"\n[ERROR] The file '{filename}' was not found.")
        print("Please make sure the file exists inside the 'logs/' folder!")

    except PermissionError:
        print(f"\n[ERROR] Access denied to '{filename}'. You don't have read permissions.")

print('\n[INFO]: Code ran successfully without crashing.')


