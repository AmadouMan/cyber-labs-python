import socket

print("===Network Port Scanner v2 ===\n")

target =input("Enter target IP: ")

start_port = 1
end_port = 1024

open_port =[]

for port in range(start_port, end_port + 1):
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    
    try:
        result = s.connect_ex((target, port))
        
        if result == 0:
            print(f"[OPEN] Port {port}")
            open_port.appen(port)
            
    except:
          pass
        
    finally:
          s.close()
print("\n=== Scan summary ===")


if open_ports:
    print(f"Open ports found:{opent_port}")
    risky_ports = [21,22,23,445,3389]
    
    for rp in risky_ports:
      if rp in open_ports:
          print(f" SOC ALERT Risky port {rp} is OPEN!")
          
else:
     print("No open ports detected.")
