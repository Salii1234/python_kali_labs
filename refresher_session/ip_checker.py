import datetime


blocked_ips = ["192.168.1.50", "10.0.0.99", "172.0.516"]
clean_ips = ["168.148.2.70", "60.4.7.69", "072.4.816"]
# We place it outside the loop to avoid it restarting everytime the loop runs
scan_count = 0 


def evaluate_ip(ip):
        if ip in blocked_ips:
            return f'[ALERT]: Warning!!!!. System at risk. Ip-address {ip} has been blacklisted, please input another address.'
        elif ip in clean_ips:
             return f'[NOTE]: IP Address {ip} is clean and safe for use.'
        else:
            return '[ERrOR]: Ip-address not found in database'
        

print('[FIREWALL INITIALIZED]: Security gatekeeper online. Type "quit" to end the sequence')

while True: 
    

    target_ip = input('\nEnter ip address to scan: ')

    if target_ip.lower() == 'quit' :
        print('[SYSTEM]: System shutting down firewall. Stay safe, operator')
        print(f'[SUMMARY]: You have scanned a total number of {scan_count} IP addresses this session.')
        break
    
    scan_count += 1
    result = evaluate_ip(target_ip)
    print("--- AUTOMATED SCAN IN PROGRESS ---")   
    print(result)

    if target_ip in blocked_ips:
         
         with open('logs/security_log.txt', 'a') as security_file:
            current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            security_file.write(f'[{current_time}][ALERT]: Blacklisted ip detected: {target_ip}\n')

    if target_ip in clean_ips:
         
         with open('logs/security_log.txt', 'a') as security_file:
            current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            security_file.write(f'[{current_time}][NOTE]: Clean ip detected: {target_ip}\n')