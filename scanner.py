import socket
import sys

def scan_port(ip, port):
    print(f"[-] Scanning {ip} on port {port}...")
    
    try:
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
    # Port 22 is SSH. Since you just used SSH to push to GitHub, 
    # we KNOW this port should be open.
    target_ip = "127.0.0.1" 
    target_port = 22
    
    scan_port(target_ip, target_port)