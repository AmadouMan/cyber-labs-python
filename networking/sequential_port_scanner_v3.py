import socket
import time

print("\n=== Simple SOC Port Scanner ===\n")

target = input("Enter target IP: ")

start_port = 1
end_port = int(input("Enter max port to scan: "))


open_ports = []

start_time = time.time()

for port in range(start_port, end_port + 1):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)

    result = s.connect_ex((target, port))

    if result == 0:
        print(f"[OPEN] Port {port}")
        open_ports.append(port)

    s.close()

end_time = time.time()

print("\n====== Scan Summary ======")

if open_ports:
    print("Open ports:", open_ports)
else:
    print("No open ports detected")

print(f"Scan duration: {round(end_time - start_time,2)} seconds")
