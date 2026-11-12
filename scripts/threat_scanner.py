incoming_requests = [
    "192.168.1.10", 
    "10.0.0.99", 
    "172.16.0.4", 
    "185.220.101.5", 
    "999.999.999"
    ]

critical_threats = ["185.220.101.5"]
suspicious_activity = ["10.0.0.99"]
authorized_ips = ["192.168.1.10", "172.16.0.4"]


def threat_scanner_evaluator(ip_address, Servrity_tag):
    if ip_address in critical_threats:
        return f'[CRITICAL THREAT] --NOTICE IP: {ip_address} HAS A SEVERITY OF AN {Servrity_tag} LEVEL'
    elif ip_address in suspicious_activity:
        return f'[SUSPICIOUS THREAT] --NOTICE IP: {ip_address} HAS A SEVERITY OF AN {Servrity_tag} LEVEL'
    elif ip_address in authorized_ips:
        return f'[AUTHORIZED IP] --NOTICE IP: {ip_address} HAS A SEVERITY OF AN {Servrity_tag} LEVEL'
    else:
        return f'[UNKNOWN IP] --NOTICE IP {ip_address} WAS NOT FOUND IN DATABASE'
    
print("--- THREAT SCAN IN PROGRESS ---")

    
for ip in incoming_requests:
    if ip in critical_threats:   
     result = threat_scanner_evaluator(ip, "DANGEROUS")
    elif ip in suspicious_activity:
        result = threat_scanner_evaluator(ip, "SUSPICIOUS")
    elif ip in authorized_ips:
        result = threat_scanner_evaluator(ip, "AUTHORIZED")
    else:
        result = threat_scanner_evaluator(ip, "NO LEVEL DETECTED") 
    print(result)
    
while True:
    user_input = input('Enter IP to scan (or type [quit] to quit) :')

    if user_input.lower() == 'quit':
        print("System terminated successfully")
        break

    result2 = threat_scanner_evaluator(user_input, Servrity_tag="STANDARD")
    print(result2)