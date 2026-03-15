import time
import re

print("\n=== SOC Real-Time SSH Brute Force Monitor v3 ===\n")

log_file = input("Enter log file path (e.g., /var/log/auth.log): ")
threshold = int(input("Enter alert threshold (e.g., 5): "))

ip_counter = {}


pattern = re.compile(r'from (\d+\.\d+\.\d+\.\d+)')

try:
    with open(log_file, "r", encoding="utf-8", errors="ignore") as f:
       
        f.seek(0, 2)
        print(f"[*] Monitoring {log_file} for failed attempts...")

        while True:
            line = f.readline()

         
            if not line:
                time.sleep(0.1)
                continue

            
            if "Failed password" in line:
                match = pattern.search(line)

                if match:
                    ip = match.group(1)

                   
                    if ip not in ip_counter:
                        ip_counter[ip] = 0
                    
                    ip_counter[ip] += 1

                    print(f"[FAILED LOGIN] {ip} → count: {ip_counter[ip]}")

                   
                    if ip_counter[ip] >= threshold:
                        print(f"🚨 SOC ALERT: Possible brute force from {ip} ({ip_counter[ip]} attempts!)")

except FileNotFoundError:
    print(f"Error: The file '{log_file}' was not found. Please check the path.")
except KeyboardInterrupt:
    print("\n[!] Monitoring stopped by user.")
