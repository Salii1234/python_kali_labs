blocked_ips = ["192.168.1.50", "10.0.0.99", "172.16.0.5"]
# We place it outside the loop to avoid it restarting everytime the loop runs
scan_count = 0 


def evaluate_ip(ip):
        if ip in blocked_ips:
            return '[ALERT]: Warning!!!!. System at risk. Ip-address inputed has been blacklisted, please input another address.'
        else:
            return '[OK]: Ip-address is safe for use'
        

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

