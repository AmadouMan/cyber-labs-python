import socket
import argparse
import threading
import time

print("\n=== SOC Network Port Scanner v3 ===\n")

parser = argparse.ArgumentParser(description="SOC Fast Port Scanner")
parser.add_argument("target", help="Target IP address")
parser.add_argument("-P", "--ports", default="1-1024", help="port range example 1-1000")

args = parser.parse_args()

target = args.target
start_port, end_port = map(int, args.ports.split("-"))
def scan_port(port):
    
    s =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    
    try:
        result = s.connect_ex((target, port))
        
        
        if result == 0:
            with lock:
                print(f"[open] port {port}")
                open_ports.append(port)
                
                
    except:
        pass
    
    finally:
        s.close()
        
        
start_time == time.time()

threads = []

for port in range(start_port, end_port + 1):
    t = threading.thread(target=scan_port, args=(port,))
    threads.append(t)
    t.start()
    
for t in threads:
    t.join()
    
end_time = time.time()

print("\n=== Scan summary ===")

if open_ports:
    print("Open ports;", open_ports)
          
    risky_ports = [21,22,23,135,445,3389]
          
    for rp in risky_ports:
          if rp in open_ports:
              print(f" SOC ALERT Risky service exposed on port {rp}")
              
else:
    print("No open ports detected.")

print(f"\nScan completed in {round(end_time - start_time,2)} seconds")            
              