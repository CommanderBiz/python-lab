import socket
import sys
from datetime import datetime


def scan_target(ip, start_port, end_port):
    print("-" * 50)
    print(f"[-] Scanning Targer: {ip}....")
    print(f"[-] Scan started at: {datetime.now()}")
    print("-" * 50)

    
    try:
        # The loop! "range" goes up to, but does NOT include the end_port,so we add 1
        for port in range(start_port, end_port + 1):
            # Create a socket object
            # AF_INET = Use IPv4
            # SOCK_STREAM = Use TCP (The handshake protocol)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
            # Don't wait more than 1 second for a reply
            s.settimeout(1)
            
            # connect_ex is like connect(), but returns an error code instead of crashing
            # 0 means Success (The port is OPEN)
            result = s.connect_ex((ip, port))
            
            if result == 0:
                print(f"[+] SUCCESS: Port {port} is OPEN!")
            else:
                print(f"[!] Port {port} is CLOSED or FILTERED.")
                
            s.close()

    except KeyboardInterrupt:
        print("\n Exiting...")
        sys.exit()
    except socket.error:
        print("\n Could not connect to server.")
        sys.exit()

       
if __name__ == "__main__":
    # We will scan "localhost" (127.0.0.1) which is your own machine 
    target_ip = "127.0.0.1" 
    
    
    # WARNING: Scanning 65535 ports takes a long time in Python. 
    # Real hackers use tools like Nmap for speed, but this teaches you the logic.
    scan_target(target_ip, 1, 1024)