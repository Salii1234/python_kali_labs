def audit_system(ip_address, scan_mode = "Standard"):
    vulnerable_ips = ['123.45.663', '133.77.85','10,54.33']
    clean_ips = ['192.168.1.1', '10.0.0.1', '172.16.0.1']

    if ip_address in vulnerable_ips:
        return f"[VULNERABILITY DETECTED] {ip_address} failed security check during {scan_mode} scan!"
    elif ip_address in clean_ips: 
        return f"[CLEAN] {ip_address} passed security check during {scan_mode} scan."
    else:
        return f"[ERROR], this ip doesn't exist in the database or provided Lists"
    
target = input('Provide IP address for credibility check: ')
result = audit_system(target)
result2 = audit_system(target, "Deep Inspection")

print(f"Security scan for inserted ip: {result}")
print(f"Results for customized deep inspection scan: {result2}")