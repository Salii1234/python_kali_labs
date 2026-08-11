#Module 4, using principles to work with files and data  

# print(' --ACCESSING NETWORK TRAFFIC-- ')

# with open('logs/network_traffic.txt', 'r') as log_file:
#     lines = log_file.readlines()

# print(lines)

# line = '10.0.0.99 - FLAGGED - 2026-08-04\n'
# omo_line = line.strip()

# print(omo_line)

# To read the lines in network.txt and to irate it sorting out the corrupted network ips from the okay ones
# print('---PARSING NETWORK LOGS FOR THREATS---')

# with open ('logs/network_traffic.txt', 'r') as log_file:
#     for line in log_file:
#         clean_line = line.strip()

#         if 'FLAGGED' in clean_line or 'CRITICAL_ALERT' in clean_line:
#             print(f'[SECURITY ALERT FOUND IN] -> {clean_line}')


#This exercise is about inserting a new file into the previous file(network.txt)
#and giving it a seperate file to store the dangerous api's (alerts_report.txt)


print("--- PARSING LOGS AND GENERATING THREAT REPORT ---")

with open('logs/network_traffic.txt', 'r') as log_file:

    with open('logs/alerts_report.txt', 'a') as report_file:
        # using the write() function to insert a text into the new file i'm creating

        report_file.write("\n--- NEW SCAN RUN: 2026-08-04 ---\n")

        #Looping directing inside log_file
        for line in log_file:
            clean_line = line.strip()

            if 'FLAGGED' in clean_line or 'CRITICAL_ALERT' in clean_line:
                report_file.write(f'[ALERT] {clean_line}\n')

print('Append new scan data to alerts_report.txt.')