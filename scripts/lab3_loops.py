# This module teaches me how to implement loops in my functions for easier working speed and after Address checking.


#AI'S CODE!!!!

# A list of target IP addresses on our network
# network_targets = [
#     "10.0.0.1",
#     "123.45.663",
#     "192.168.1.50",
#     "133.77.85",
#     "172.16.0.1"
# ]

# vulnerable_ips = ["123.45.663", "133.77.85", "10.54.33"]

# print("--- STARTING AUTOMATED NETWORK SCAN ---")

# # The 'for' loop iterates over each IP in 'network_targets'
# for ip in network_targets:
#     if ip in vulnerable_ips:
#         print(f"[ALERT] Vulnerability detected on {ip}!")
#     else:
#         print(f"[CLEAN] {ip} passed inspection.")

# print("--- SCAN COMPLETE ---")

#Implementing the audit_system with this for loop idea.

network_addresses = [
    '123.45.663', 
    '192.168.1.1',
    '133.77.85',
    '10.0.0.1',
    '172.16.0.1',
    '10.54.33'
]

vulnerable_ips = ['123.45.663', '133.77.85','10.54.33']
     
clean_ips = ['192.168.1.1', '10.0.0.1', '172.16.0.1']     



def audit_system(ip_address, scan_mode = "STANDARD"):
    if ip_address in vulnerable_ips :
        return f"[ALERT] ---{ip_address} INSERTED IP MAY BE CORRUPTED, PLEASE TAKE {scan_mode} MODE --- "
    elif ip_address in clean_ips :
        return f'[CLEAN] ---IP {ip_address} HAS NO THREATS, PLEASE TAKE {scan_mode} ---'
    else:
        return '[ERROR] --IP ADDRESS NOT FOUND IN DATABASE'
    
print("--- AUTOMATED SCAN IN PROGRESS ---")    



for ip in network_addresses:
    result  = audit_system(ip)
    print(f'Audit system recieving network address: {result}')


while True:
    user_input = input('Enter IP to scan (or type [exit] to quit) :' )

    if user_input.lower() == 'exit':
        print("User as exited successfully")
        break 


    target = audit_system(user_input)
    print(target)