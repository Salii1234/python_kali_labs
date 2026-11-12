import socket

print('[FILE SYNC IN PROGRESS]')

# Open the target file and read it line by line
with open('target.txt', 'r') as file_name:
    for line in file_name:
        # Strip invisible spaces and newline characters (\n)
        target_ip = line.strip()

        # Skip empty lines if any exist in the text file
        if not target_ip:
            continue

        print(f"\n--- Scanning Target: {target_ip} ---")
        print('-' * 50)

        ports_to_scan = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3389, 3306]

        try:
            for port in ports_to_scan:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(0.5)
                result = s.connect_ex((target_ip, port))

                if result == 0:
                    print(f'[+] Port {port} is open on {target_ip}')
                    banner = s.recv(1024).decode('utf-8', errors='ignore').strip()
                    if banner:
                        print(f'    [+] Banner: {banner}')
                    else:
                        print('    [+] No banner received.')
                else:
                    print(f'[-] Port {port} is closed on {target_ip}')

                s.close()
        
        except socket.error:
            print(f'[-] Could not connect to {target_ip}')
        except Exception as e:
            print(f'[-] An error occurred: {e}')