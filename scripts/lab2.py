# A function is used when I want to perform multiple taks without haveing to write numerous lines of code
# I can just create a simple function and stores all those lines of code into one organized block.

# def check_password_strength(password):
#    if len(password) < 8:
#       return "weak ahh password"
#    else:
#       return "secure password"
   

# test_sumation = check_password_strength("DavidOl123")
# print(f"The password provided is a {test_sumation}")

    
#Exercise.

# def ip_access_control(ip_address, blocked_ips):
#     print(f"Proceed checking for ip {ip_address}")
#     if ip_address in blocked_ips:
#       return "Access Denied,ip address is blacklisted."
#     else:
#       return "Access Granted son"

# ip_correct_confirmation = ip_access_control("193.22.578", ["145.67.78", "193.22.578","34.86.95"])
# ip_wrong_confirmation = ip_access_control("124.67.45", ["272.44.89", "229.55.89", "39.11.945"])
# print(f"The result for this ip confirmation is {ip_correct_confirmation}, while this result is {ip_wrong_confirmation}")


#Exercise 2

def firewall_check(ip_address, default_port = 80):
    blocked_ips = ["193.56.89", "10.0.0.6"]

    if ip_address in blocked_ips:
        return f"an [ALERT] IP {ip_address} is BLOCKED on port {default_port}!"
    else:
        return f"[OK]. Traffic allowed from {ip_address} on port {default_port}."

target = input('Enter target IP to test through firewall: ')

result = firewall_check(target)
print(f'The result is {result}')


