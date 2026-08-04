# Your Mission: log_parser.py
# Write a brand new script called log_parser.py that:

# Opens raw_firewall.log in read mode.

# Extracts ONLY the lines that contain "BLOCKED".

# Saves those blocked entries into a file named blocked_threats.txt.

# Prints a summary count to the console when finished (e.g., Scan complete: 3 blocked IPs saved to blocked_threats.txt).

blocked_counter = 0

with open('raw_firewall.log', 'r') as firewall_file:
    with open('blocked_threats.log', 'w') as block_files:

        block_files.write('=== BLOCKED FILE SORTING PROCEDURE ===\n\n')

        for line in firewall_file:
            clean_line = line.strip()

            if 'BLOCKED' in clean_line:
                block_files.write (f'[ALERT] -> {clean_line}\n')
                print(f'[BLOCKED FILE] -> {clean_line}')
                blocked_counter += 1
    
    with open('blocked_threats.log', 'a') as parser_file:
        parser_file.write('\n--- NEW SCAN RUN: 2026-08-04 ---\n')

print(f"Scan complete: {blocked_counter} blocked IPs saved to blocked_threats.txt")  
         
         