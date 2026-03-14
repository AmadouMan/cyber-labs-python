import socket

print("=== Network Port Scanner v1 ===")

target = "127.0.0.1"

ports = [21,22,23,25,53,80,110,139,143,443,445,3389]

for port in ports:
    s = socket.socket()
    s.settimeout(1)
    
    result = s.connect_ex((target, port))
    
    if result == 0:
        print(f"[OPEN] port {port}")
    else:
        print(f"[CLOSED] Port {port}")
        
    s.close()
    
print("\nScan finished.")   
      
