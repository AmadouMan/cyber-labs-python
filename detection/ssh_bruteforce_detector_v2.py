import re

print("\n=== SOC SSH Brute Force Detector v2 ===\n")

log_file = input("Enter log file path: ")
threshold = int(input("Enter alert threshold: "))

ip_counter = {}

pattern = re.compile(r'from (\d+\.\d+\.\d+\.\d+)')

with open(log_file, "r", encoding="utf-8", errors="ignore") as f:
    for line in f:
        if "Failed password" in line:

            match = pattern.search(line)

            if match:
                ip = match.group(1)

                if ip not in ip_counter:
                    ip_counter[ip] = 0

                ip_counter[ip] += 1

print("\n====== Detection Report ======")

for ip, count in ip_counter.items():
    if count >= threshold:
        print(f"[ALERT] Possible brute force from {ip} ({count} attempts)")
    else:
        print(f"[INFO] {ip} failed attempts: {count}")