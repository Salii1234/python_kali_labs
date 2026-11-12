# import socket
# from datetime import datetime
# #import the libaries we need.

# # Target host: We'll target localhost (your own machine) for safe testing
# target_host = "127.0.0.1"

# # A small list of common ports to check (FTP, SSH, HTTP, HTTPS, Alt-HTTP)
# ports_to_scan = [21, 22, 80, 443, 8080]

# print('-' * 50)
# print(f'Scanning target: {target_host}')
# #To get the date the scan started.
# print(f'Scan started at: {str(datetime.now())}')
# print('-' * 50)


# try:
#     for port in ports_to_scan:
#         # creating the socket object
#         # AF_INET specifies IPv4, SOCK_STREAM specifies TCP
#         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#         # set a timer so the script doesn't crash trying to look for an recipent
#         s.settimeout(1.0)

#         # to really know if its opened or closed, we use s.connect_ex()
#         # create new variable 'result'

#         result = s.connect_ex((target_host, port))


#         if result == 0:
#             print(f'[+] Port {port}: OPEN')
#         else:
#             print(f'[-] Port {port}: CLOSED')

#         s.close()

# except KeyboardInterrupt:
#     print("\n[!] Operation cancelled by user.")
# except socket.gaierror:
#     print("\n[!] Hostname could not be resolved.")
# except socket.error:
#     print("\n[!] Could not connect to server.")


# print('-' * 50)
# print('Scan complete')

# Now we want to add an input function to make it interactive
# And we want to also add a total time function to count the total time it took to run the code.

import socket
from datetime import datetime

print('-' * 50)
print('[CODE BASE]: Begin ip scanner V2..')


# create variable for input function
target_input = input('Input ip address of choice (e.g ., 127.0.0.1): ')

try:
    target_host = socket.gethostbyname(target_input)
except socket.gaierror:
    print('\n!Invalid IP address or hostname given.')
    exit()

ports_to_scan = [21, 22, 80, 443, 3306, 8080]

print('-' * 50)
print(f'Host to scan: {target_host}')
scan_start_time = datetime.now()
print(f'Scan started at: {scan_start_time}')
print('-' * 50)

try:
    for port in ports_to_scan:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2.0)

        result = s.connect_ex((target_host, port))

        if result == 0:
            print(f'Port {port}: OPEN')
            #Banner gathering. To get more details of our ports
            try:
                s.settimeout(1.0)

                banner = s.recv(1024) .decode('utf-8', errors='ignore').strip()

                if banner:
                    print(f' [+] Banner: {banner}')
                else:
                    print('  [-] Service open, but banner failed to return')
            except Exception:
                print('[-] Could not retrieve banner')
        else: 
            print(f'Port {port}: CLOSED')

        s.close()

except socket.error:
    print('\n[!] Socket connection failed.')
except KeyboardInterrupt:
    print('\n[!] Operation cancelled by user.')



print('-' * 50)
print('Scan complete')
