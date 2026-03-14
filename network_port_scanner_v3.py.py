import socket
import argparse
import time

print("\n=== SOC Network Port Scanner v3 ===\n")

# ---------- CLI Arguments ----------
parser = argparse.ArgumentParser(description="SOC Network Port Scanner")

parser.add_argument("target", help="Target IP address to scan")
parser.add_argument("-p", "--ports", default="1-1024",
                    help="Port range example: 1-500")

args = parser.parse_args()

target = args.target

# ---------- Port Range ----------
start_port, end_port = map(int, args.ports.split("-"))

open_ports = []

# ---------- Start Timer ----------
end_time = time.time()

print(f"Scanning target: {target}")
print(f"Port range: {start_port}-{end_port}\n")

# ---------- Scan Loop ----------
for port in range(start_port, end_port + 1):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)

    try:
        result = s.connect_ex((target, port))

        if result == 0:
            print(f"[OPEN] Port {port}")
            open_ports.append(port)

    except:
        pass

    finally:
        s.close()

# ---------- End Timer ----------
end_time = time.time()

# ---------- Summary ----------
print("\n========== Scan Summary ==========")

if open_ports:
    print("Open Ports Found:")
    for p in open_ports:
        print(f" - {p}")
else:
    print("No open ports detected.")

print(f"\nScan Duration: {round(end_time - start_time, 2)} seconds")
print("==================================")
