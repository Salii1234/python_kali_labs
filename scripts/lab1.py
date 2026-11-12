# Variables and Loops classes.

#Variables are used whenever my program needs to remember a piece of information so it can use or change it later.

target_host = '192.168.1.50'
ports_available = 4
scan_complete = False
decimal_plate = 0.95

#print(target_host)

#Conditionals. These are used to execute specific actions based on a condition being true or false.

target_ports = 0

# if target_ports > 0:
#  print("Vunerabilities found in the system")
# else: 
#  print("System appears safe")


#  security_level = 'low'

#  if security_level == 'high':
#   print("Firewall Strict Mode Active")
#  else:
#   print("Firewall Standard mode Active")

#Elif (Multiple choice statements)

open_ports = 10

# if open_ports == 0:
#     print("System secure: No open ports found")
# elif open_ports <= 3:
#     print("Low Risk: Few open ports")
# elif open_ports <= 10:
#     print("Medium risk: Multiple open ports detected")
# else:
#     print("HIGH RISK!!!: Critical number of open ports!")



# A while loop is used if I want a condition to run until a certain perequsite is met.
# For instant,in the code below,I want the port to be scanned at least 5 times before it has been fully scanned.

# port = 1

# while port <= 5:
#     print("Scanning port number....")
#     print(port)
#     port = port + 1
# print("Scanned computer")


# For loop. Its used when I want to iterate to a list of items automatically and there is no increment step required to do so.

# #for list of numbers
# for port in range(1,6):
#     print("Scanning Port")
#     print(port)

# #for list of items
# target_ips = ['192.34.22', '09.38.444', '172.829.32']

# for ip in target_ips:
#     print("Scanning port")
#     print(ip)

#Exercise.


# passwords = ['123456', 'drugLove', 'SayMyName248IloveLatinas','72hours34']

# for word in passwords:
#     print("Testing password credibility")
#     print(word)
# print("Brute force attack completed")



#Exercise
# Correct_password = 'SayMyName248IloveLatinas'
# Potiental_passwords = ['loveMEIrl', 'SayMyName248IloveLatinas','SwaggerLifor1','DesmondISaFraud']

# for word in Potiental_passwords:
#     print("Testing credibility for password.." + word)
#     if word == Correct_password:
#         print("Password Matched")
#         break
#     else:
#         print("Couldn't matched password for potiental word.." + word)

# print('Breach successful')


#Exercise 2.

target_ip = '192.168.1.100'
vulnerable_port = 80
port_to_scan  = [21,22,80,443,3389]

for port in port_to_scan:
    print("Checking credibility of ports in List")
    if port == vulnerable_port:
        print("This port is vunlerable and open, ensure security measures")
        break
    else:
        print(f"Port {port} is secure")
    
print(f"Scan completed for {target_ip} has been concluded")

